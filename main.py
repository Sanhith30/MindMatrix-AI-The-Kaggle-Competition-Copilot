import os
from dotenv import load_dotenv
from src.agents import MindMatrixAgent
from termcolor import colored

# Load environment variables
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(colored("Error: GEMINI_API_KEY not found in .env file", "red"))
        return

    # Initialize the Agent
    agent = MindMatrixAgent(api_key)

    print(colored("=============================================", "magenta"))
    print(colored("   MindMatrix AI - Kaggle Competition Agent  ", "magenta", attrs=['bold']))
    print(colored("=============================================", "magenta"))
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input(colored("> Enter competition name (e.g. 'titanic'): ", "yellow"))
        
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        # Run the agent
        response = agent.run(f"I want to participate in the '{user_input}' competition. Please set up the workspace and create a baseline submission.")
        
        print(colored("\n[MindMatrix Final Response]:", "green", attrs=['bold']))
        print(response)
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    main()