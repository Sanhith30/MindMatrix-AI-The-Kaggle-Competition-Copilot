import google.generativeai as genai
from termcolor import colored
from .tools import KaggleTools

class MindMatrixAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        
        # Initialize Tools
        self.kt = KaggleTools()
        
        # Define the tools available to Gemini
        self.tools_list = [
            self.kt.list_competitions,
            self.kt.download_data,
            self.kt.inspect_csv,
            self.kt.save_code_to_file
        ]
        
        # Initialize the Model
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", # Use 'pro' if you have access
            tools=self.tools_list,
            system_instruction="""
                You are MindMatrix, an expert Data Science Agent.
                Your mission is to help the user win Kaggle competitions.
                
                You have a strict workflow:
                1. SEARCH for the competition name the user gives you.
                2. DOWNLOAD the dataset for that competition.
                3. INSPECT the 'train.csv' (or similar) to understand the features and target variable.
                4. REASON about the best model (e.g., "This is a classification problem, I will use Random Forest").
                5. WRITE a complete Python script (submission.py) that loads the data, trains a model, and saves 'submission.csv'.
                6. USE the 'save_code_to_file' tool to save your script.
                
                Always confirm to the user when a step is done.
            """
        )
        
        # Start a chat session (Memory)
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def run(self, user_input: str):
        print(colored(f"\n[MindMatrix] Analyzing request: {user_input}", "green"))
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"