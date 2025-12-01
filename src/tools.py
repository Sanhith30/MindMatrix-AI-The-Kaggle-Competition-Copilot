import os
import kaggle
import pandas as pd
from termcolor import colored

class KaggleTools:
    """
    A collection of tools to interact with the Kaggle platform
    and local filesystem.
    """

    def list_competitions(self, search_term: str):
        """Searches for Kaggle competitions based on a keyword."""
        print(colored(f"  [Tool] Searching Kaggle for: {search_term}...", "cyan"))
        try:
            api = kaggle.KaggleApi()
            api.authenticate()
            comps = api.competitions_list(search=search_term)
            # Return top 3 results to save tokens
            result = [(c.ref, c.category) for c in comps[:3]]
            return f"Found competitions: {result}"
        except Exception as e:
            return f"Error searching competitions: {str(e)}"

    def download_data(self, competition_ref: str):
        """Downloads and unzips competition data to a local folder."""
        print(colored(f"  [Tool] Downloading data for: {competition_ref}...", "cyan"))
        try:
            api = kaggle.KaggleApi()
            api.authenticate()
            target_path = f"./kaggle_data/{competition_ref}"
            os.makedirs(target_path, exist_ok=True)
            
            api.competition_download_files(competition_ref, path=target_path, unzip=True)
            
            # List files to show the agent what it got
            files = os.listdir(target_path)
            return f"Data downloaded to {target_path}. Files found: {files}"
        except Exception as e:
            return f"Error downloading data: {str(e)}"

    def inspect_csv(self, file_path: str):
        """Reads the first 5 rows of a CSV file to understand the schema."""
        print(colored(f"  [Tool] Inspecting file: {file_path}...", "cyan"))
        try:
            # Handle potential relative paths
            if not os.path.exists(file_path):
                # Try looking in kaggle_data if path is just a filename
                for root, dirs, files in os.walk("./kaggle_data"):
                    if file_path in files:
                        file_path = os.path.join(root, file_path)
                        break
            
            df = pd.read_csv(file_path)
            info = (
                f"Columns: {list(df.columns)}\n"
                f"Data Types:\n{df.dtypes}\n"
                f"First 3 Rows:\n{df.head(3).to_string()}"
            )
            return info
        except Exception as e:
            return f"Error reading CSV: {str(e)}"

    def save_code_to_file(self, filename: str, code_content: str):
        """Saves generated python code to a file."""
        print(colored(f"  [Tool] Saving code to: {filename}...", "cyan"))
        try:
            with open(filename, 'w') as f:
                f.write(code_content)
            return f"Successfully saved code to {filename}. You can now run this script."
        except Exception as e:
            return f"Error saving file: {str(e)}"