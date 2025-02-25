import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI


def ask_chatgpt(azure_oai_endpoint, azure_oai_key, azure_oai_deployment, text):
    """Funktion för att skicka en vanlig GPT-förfrågan utan datakälla."""

    # Skapa en ny klient för att fråga ChatGPT utan extensions
    client = AzureOpenAI(
        base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}",
        api_key=azure_oai_key,
        api_version="2023-09-01-preview"
    )

    response = client.chat.completions.create(
        model=azure_oai_deployment,
        temperature=0.5,
        max_tokens=1000,
        messages=[
            {"role": "system", "content": "You are a helpful travel agent"},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content


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

        # Skapa en klient som inkluderar extensions (för sökning)
        client = AzureOpenAI(
            base_url=f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/extensions",
            api_key=azure_oai_key,
            api_version="2023-09-01-preview"
        )

        # Get the prompt
        text = input('\nEnter a question:\n')

        # Configure search extension
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

        # Försök att hämta svar från Cognitive Search
        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.5,
            max_tokens=1000,
            messages=[
                {"role": "system", "content": "You are a helpful travel agent"},
                {"role": "user", "content": text}
            ],
            extra_body=extension_config  # Använd Search
        )

        response_text = response.choices[0].message.content

        # Om svaret säger att ingen information hittades, försök med ChatGPT utan extensions
        if "not found in the retrieved data" in response_text.lower():
            print("\nInget hittades i filerna, försöker med ChatGPT...\n")
            response_text = ask_chatgpt(
                azure_oai_endpoint, azure_oai_key, azure_oai_deployment, text)

        # Print final response
        print("\n" + response_text + "\n")

    except Exception as ex:
        print("Error:", ex)


if __name__ == '__main__':
    main()
