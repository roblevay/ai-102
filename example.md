
To adapt the provided Azure AI Agent Service exercise to use Visual Studio Code (VSCode) with local file paths in your `c:\ai-102` directory, which contains the `ai-agents` subdirectory, you'll need to set up a local development environment on your machine. This involves installing necessary tools, organizing the project files locally, and modifying the instructions to run the application in VSCode instead of the Azure Cloud Shell. Below, I'll rewrite the exercise instructions to reflect these changes, ensuring the code runs locally in VSCode using the paths you specified (e.g., `c:\ai-102\ai-agents`).

The rewritten instructions will assume you have the `ai-agents` repository files already in `c:\ai-102\ai-agents` (e.g., from cloning the GitHub repository locally or copying them from another source). If you haven't set up the repository yet, I'll include steps to clone it locally. The instructions will also guide you through setting up Python, installing dependencies, configuring VSCode, and running the application locally.

---

# Develop an AI Agent Using VSCode with Local File Paths

In this exercise, you'll use the Azure AI Agent Service to create a simple agent that analyzes data and creates charts, using the built-in *Code Interpreter* tool to dynamically generate code. The exercise has been adapted to run locally in Visual Studio Code (VSCode) using the local directory `c:\ai-102\ai-agents` instead of the Azure Cloud Shell.

> **Tip**: The code used in this exercise is based on the Azure AI Foundry SDK for Python. You can develop similar solutions using the SDKs for Microsoft .NET, JavaScript, and Java. Refer to [Azure AI Foundry SDK client libraries](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/sdk-overview) for details.

This exercise should take approximately **30** minutes to complete.

> **Note**: Some of the technologies used in this exercise are in preview or in active development. You may experience some unexpected behavior, warnings, or errors.

## Prerequisites

Before starting, ensure you have the following installed on your local machine:
- **Python 3.8 or later**: Download and install from [python.org](https://www.python.org/downloads/). Ensure Python is added to your system PATH.
- **Visual Studio Code**: Download and install from [code.visualstudio.com](https://code.visualstudio.com/).
- **VSCode Python Extension**: Install the Python extension in VSCode for Python support.
- **Git**: Install from [git-scm.com](https://git-scm.com/) to clone the repository (if not already done).
- **Azure CLI**: Install from [Azure CLI installation](https://learn.microsoft.com/cli/azure/install-azure-cli) to authenticate with Azure.
- An active Azure subscription with access to Azure AI Foundry and a deployed **gpt-4o** model.

## Create an Azure AI Foundry Project

1. In a web browser, open the [Azure AI Foundry portal](https://ai.azure.com) at `https://ai.azure.com` and sign in using your Azure credentials. Close any tips or quick start panes, and navigate to the home page using the **Azure AI Foundry** logo if necessary.
2. On the home page, select **Create an agent**.
3. When prompted to create a project, enter a valid name and expand **Advanced options**.
4. Confirm the following settings:
   - **Azure AI Foundry resource**: A valid name for your Azure AI Foundry resource.
   - **Subscription**: Your Azure subscription.
   - **Resource group**: Create or select a resource group.
   - **Region**: Select any **AI Services supported location**.
   > **Note**: Some Azure AI resources are constrained by regional model quotas. You may need to create another resource in a different region if quota limits are exceeded later.
5. Select **Create** and wait for your project to be created.
6. If prompted, deploy a **gpt-4o** model using either the *Global Standard* or *Standard* deployment option (depending on your quota availability).
   > **Note**: If quota is available, a GPT-4o base model may be deployed automatically when creating your agent and project.
7. When your project is created, the Agents playground will open.
8. In the navigation pane on the left, select **Overview** to view the project’s main page.
9. Copy the **Azure AI Foundry project endpoint** and **model deployment name** (should be *gpt-4o*) to a text editor (e.g., Notepad) for use later.

## Set Up the Local Development Environment in VSCode

### Clone or Verify the Repository

1. If you haven’t already placed the `ai-agents` repository in `c:\ai-102\ai-agents`, clone it locally:
   - Open a Command Prompt or PowerShell terminal.
   - Navigate to the `c:\ai-102` directory:
     ```
     cd c:\ai-102
     ```
   - Clone the GitHub repository:
     ```
     git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
     ```
   - Verify the files are in `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python`, which should include `agent.py`, `.env`, `requirements.txt`, and `data.txt`.

2. Open VSCode:
   - Launch VSCode.
   - Select **File > Open Folder** and choose `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python`.

3. Ensure the Python extension is installed in VSCode:
   - Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).
   - Search for “Python” and install the official Python extension by Microsoft if not already installed.

4. Select the Python interpreter:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P`) to open the Command Palette.
   - Type `Python: Select Interpreter` and select your Python 3.8+ installation (e.g., `Python 3.x.x`).

### Configure the Application Settings

1. Create a virtual environment in the project folder:
   - In VSCode, open the integrated terminal (`Ctrl+`` or View > Terminal`).
   - Ensure you’re in the `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python` directory:
     ```
     cd c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python
     ```
   - Create a virtual environment:
     ```
     python -m venv labenv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .\labenv\Scripts\Activate.ps1
       ```
     - On macOS/Linux:
       ```
       source labenv/bin/activate
       ```

2. Install the required Python packages:
   - In the activated virtual environment, run:
     ```
     pip install -r requirements.txt azure-ai-projects
     ```

3. Configure the `.env` file:
   - In VSCode, open the `.env` file located in `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python`.
   - Replace the **your_project_endpoint** placeholder with the endpoint copied from the Azure AI Foundry portal.
   - Ensure the `MODEL_DEPLOYMENT_NAME` variable is set to `gpt-4o` (or your deployed model name).
   - Example `.env` content:
     ```
     PROJECT_ENDPOINT=https://your-resource-name.region.ai.azure.com/
     MODEL_DEPLOYMENT_NAME=gpt-4o
     ```
   - Save the file (`Ctrl+S`).

## Write Code for the Agent Application

The `agent.py` file in `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python` contains the base code for the agent application. You’ll edit it in VSCode to implement the AI agent.

1. Open `agent.py` in VSCode:
   - In the Explorer pane, navigate to `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python` and open `agent.py`.

2. Review the existing code, which loads configuration settings from `.env` and data from `data.txt`. The file includes comments where you’ll add code to implement the agent.

3. Add the necessary code by following the comments in `agent.py`. Below is the complete code for reference, with the sections you need to add (ensure proper indentation, matching the existing comments):

   ```python
   import os
   from dotenv import load_dotenv

   # Load configuration settings
   load_dotenv()
   project_endpoint = os.getenv("PROJECT_ENDPOINT")
   model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")
   file_path = "data.txt"

   # Load data to be analyzed
   with open(file_path, "r") as file:
       data = file.read()
   print("Loaded data:\n")
   print(data)

   # Add references
   from azure.identity import DefaultAzureCredential
   from azure.ai.agents import AgentsClient
   from azure.ai.agents.models import FilePurpose, CodeInterpreterTool, ListSortOrder, MessageRole

   # Connect to the Agent client
   agent_client = AgentsClient(
       endpoint=project_endpoint,
       credential=DefaultAzureCredential(
           exclude_environment_credential=True,
           exclude_managed_identity_credential=True
       )
   )
   with agent_client:
       # Upload the data file and create a CodeInterpreterTool
       file = agent_client.files.upload_and_poll(
           file_path=file_path,
           purpose=FilePurpose.AGENTS
       )
       print(f"Uploaded {file.filename}")

       code_interpreter = CodeInterpreterTool(file_ids=[file.id])

       # Define an agent that uses the CodeInterpreterTool
       agent = agent_client.create_agent(
           model=model_deployment,
           name="data-agent",
           instructions="You are an AI agent that analyzes the data in the file that has been uploaded. Use Python to calculate statistical metrics as necessary.",
           tools=code_interpreter.definitions,
           tool_resources=code_interpreter.resources,
       )
       print(f"Using agent: {agent.name}")

       # Create a thread for the conversation
       thread = agent_client.threads.create()

       while True:
           user_prompt = input("\nEnter your prompt (or 'quit' to exit): ")
           if user_prompt.lower() == "quit":
               break

           # Send a prompt to the agent
           message = agent_client.messages.create(
               thread_id=thread.id,
               role="user",
               content=user_prompt,
           )

           run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

           # Check the run status for failures
           if run.status == "failed":
               print(f"Run failed: {run.last_error}")

           # Show the latest response from the agent
           last_msg = agent_client.messages.get_last_message_text_by_role(
               thread_id=thread.id,
               role=MessageRole.AGENT,
           )
           if last_msg:
               print(f"Last Message: {last_msg.text.value}")

       # Get the conversation history
       print("\nConversation Log:\n")
       messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
       for message in messages:
           if message.text_messages:
               last_msg = message.text_messages[-1]
               print(f"{message.role}: {last_msg.text.value}\n")

       # Clean up
       agent_client.delete_agent(agent.id)
   ```

4. Save the file (`Ctrl+S`).

5. Verify the code:
   - Ensure all added code aligns with the comments’ indentation (typically 4 spaces per level).
   - The code connects to the Azure AI Foundry project, uploads `data.txt`, creates an agent with the Code Interpreter tool, runs a conversation thread, and cleans up resources.

## Sign into Azure and Run the Application

1. Authenticate with Azure CLI:
   - In the VSCode terminal (ensure the virtual environment is activated: `.\labenv\Scripts\Activate.ps1` on Windows or `source labenv/bin/activate` on macOS/Linux).
   - Run:
     ```
     az login
     ```
   - Follow the prompts to open a browser, enter the authentication code, and sign in with your Azure credentials. If you have multiple subscriptions, select the one containing your Azure AI Foundry resource:
     ```
     az account set --subscription "Your-Subscription-Name-or-ID"
     ```

2. Run the application:
   - In the VSCode terminal, ensure you’re in `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python`.
   - Run:
     ```
     python agent.py
     ```

3. Interact with the agent:
   - The application loads and displays the data from `data.txt`.
   - Enter a prompt, such as:
     ```
     What's the category with the highest cost?
     ```
   - View the response, then try another prompt:
     ```
     Create a text-based bar chart showing cost by category
     ```
   - Try a statistical prompt:
     ```
     What's the standard deviation of cost?
     ```
   - Continue entering prompts (the thread retains conversation history). Enter `quit` to exit.

4. Review the conversation log displayed after quitting, which includes all messages, including any agent-generated steps from the Code Interpreter tool.

> **Tip**: If the app fails due to rate limits, wait a few seconds and retry. If quota is insufficient, check your Azure AI Foundry resource or try a different region.

## Debug in VSCode (Optional)

If you encounter issues:
- Set breakpoints in `agent.py` by clicking next to line numbers in VSCode.
- Press `F5` to start debugging, selecting the “Python” configuration.
- Use the Debug Console and Variables pane to inspect values and step through the code.

## Summary

In this exercise, you adapted the Azure AI Agent Service exercise to run locally in VSCode using the `c:\ai-102\ai-agents` directory. You set up a local Python environment, configured the application, and ran an AI agent that uses the Code Interpreter tool to analyze data and generate responses.

## Clean Up

To avoid unnecessary Azure costs, delete the resources created:
1. Open the [Azure portal](https://portal.azure.com).
2. Navigate to the resource group containing your Azure AI Foundry resources.
3. Select **Delete resource group**, enter the resource group name, and confirm deletion.

---

### Key Changes Made
1. **Local File Paths**: Instructions use `c:\ai-102\ai-agents\Labfiles\02-build-ai-agent\Python` as the working directory.
2. **VSCode Integration**: Steps guide you to use VSCode for editing and running `agent.py`, including setting up the Python extension and virtual environment.
3. **Local Setup**: Replaced Cloud Shell commands with local terminal commands for cloning the repository, creating a virtual environment, and installing dependencies.
4. **Azure CLI**: Used `az login` locally for authentication, with guidance for multi-tenant scenarios.
5. **Code Unchanged**: The Python code in `agent.py` remains identical to the original, as it’s compatible with local execution. Only the setup and execution environment changed.

If you encounter issues (e.g., missing files, authentication errors, or quota limits), let me know, and I can provide specific troubleshooting steps!
