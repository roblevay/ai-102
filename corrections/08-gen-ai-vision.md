Här är din uppdaterade instruktion i **korrekt och aktuell form**, anpassad för Azure AI Studio med nya SDK\:n (`azure-ai-resources`). Allt är i **Markdown-format** och redo att klistras in i en dokumentation eller labb:

---

## 🛠️ Instruktioner för att ansluta till en GPT-modell i Azure AI Studio-projekt

1. I kodfilen, notera de befintliga import-satserna i början av filen. Leta sedan upp kommentaren **Add references**, och uppdatera med följande kod för att referera till rätt bibliotek du tidigare installerat:

   ```python
   # Add references
   from azure.identity import DefaultAzureCredential
   from azure.ai.resources.client import AIClient
   from openai import AzureOpenAI
   ```

2. I funktionen **main**, under kommentaren **Get configuration settings**, notera att koden laddar projektets anslutningsinformation och det modellnamn du har definierat i `.env`-filen.

3. Under kommentaren **Initialize the project client**, ersätt eventuell gammal kod och lägg till följande kod för att ansluta till ditt Azure AI Studio-projekt:

   > 💡 **Tips:** Kom ihåg att behålla rätt indenteringsnivå i din kod.

   ```python
   # Initialize the project client
   ai_client = AIClient.from_config(
       credential=DefaultAzureCredential(
           exclude_environment_credential=True,
           exclude_managed_identity_credential=True
       )
   )
   ```

4. Hitta kommentaren **Get a chat client**, och ersätt eventuell tidigare kod med följande kod för att skapa en klient för att kommunicera med GPT-modellen:

   ```python
   # Get a chat client
   openai_client = ai_client.get_azure_openai_client(api_version="2024-10-21")
   ```

---

Vill du att jag sammanställer dessa steg som en komplett README-fil till ditt projekt också?
