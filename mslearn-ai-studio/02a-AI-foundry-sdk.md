### Prepare the application configuration

Start VSCode and open the folder where your ai-exercises reside, for example c:\ai

1. Open a terminal and run the command (replace c:\ai with the name of your folder)

    ```
   cd c:\ai
     ```

    and then
   ```
   rm -r mslearn-ai-foundry -Force -ErrorAction SilentlyContinue
    ```
    and

   ```
     git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry

     ```

    

4. After the repo has been cloned, navigate to the folder containing the chat application code files :

    ```
   cd mslearn-ai-foundry/labfiles/chat-app/python
    ```

    The folder contains a code file as well as a configuration file for application settings and a file defining the project runtime and package requrirements.

1. In the cloud shell command-line pane, enter the following command to install the libraries you'll use:

    ```
   python -m venv labenv
   ./labenv/bin/Activate.ps1
   pip install -r requirements.txt azure-identity azure-ai-projects openai
    ```
