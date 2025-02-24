import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI


def main():
    try:
        # Load configuration
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        azure_search_key = os.getenv("AZURE_SEARCH_KEY")
        azure_search_index = os.getenv("AZURE_SEARCH_INDEX")

        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/extensions",
            api_key=azure_oai_key,
            api_version="2023-09-01-preview"
        )

        # Get the prompt
        text = input('\nEnter a question:\n')

        # Configure your data source
        extension_config = dict(dataSources=[
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": azure_search_endpoint,
                    "key": azure_search_key,
                    "indexName": azure_search_index,
                }
            }
        ])

        # Send request to Azure OpenAI model with search extension
        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.5,
            max_tokens=1000,
            messages=[
                {"role": "system", "content": "You are a helpful travel agent"},
                {"role": "user", "content": text}
            ],
            extra_body=extension_config
        )

        # Extract response text
        response_text = response.choices[0].message.content

        # Extract citations and replace [doc1], [doc2] with real names
        try:
            citations = response.choices[0].message.context.get("messages", [{}])[
                0].get("content", "{}")
            citation_json = json.loads(citations)

            if "citations" in citation_json:
                doc_mapping = {}
                for idx, c in enumerate(citation_json["citations"], start=1):
                    doc_name = c.get("title", f"Unknown Document {idx}")
                    doc_ref = f"[doc{idx}]"  # Match format i svaret
                    # Lägg till klamrar och mellanslag
                    formatted_name = f"[ {doc_name} ]"
                    # Skapa en mapping mellan generiskt namn och riktigt namn
                    doc_mapping[doc_ref] = formatted_name

                # Ersätt generiska [docX] i svaret med de riktiga dokumentnamnen
                for doc_ref, real_name in doc_mapping.items():
                    response_text = response_text.replace(doc_ref, real_name)

        except Exception:
            pass  # Om det blir fel, skriv inte ut något extra

        # Print only the final updated response
        print("\n" + response_text + "\n")

    except Exception as ex:
        print("Error:", ex)


if __name__ == '__main__':
    main()
