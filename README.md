# MindMatrix AI - Kaggle Competition Assistant

**MindMatrix** is an intelligent agentic workflow designed to automate the "cold start" phase of Kaggle competitions. Powered by **Google Gemini 1.5**, it autonomously searches for competitions, analyzes dataset schemas, and generates baseline submission code.

## 🏗️ Architecture
The system follows a **Single-Agent with Tools** architecture:
1.  **Brain:** Gemini 1.5 Flash (via `google.generativeai`).
2.  **Memory:** Uses Gemini's chat session history to retain context about dataset columns.
3.  **Tools:** * `KaggleAPI`: For searching and downloading data.
    * `Pandas`: For inspecting CSV headers and data types.
    * `FileSystem`: For saving generated Python scripts.

## 🚀 How to Run

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd MindMatrix-Kaggle-Agent
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Keys**
    * Get your Gemini API Key from Google AI Studio.
    * Get your `kaggle.json` from your Kaggle Account Settings.
    * Create a `.env` file and add:
        ```
        GEMINI_API_KEY=your_key_here
        ```
    * Ensure `kaggle.json` is in your `~/.kaggle/` folder or configured in the environment.

4.  **Run the Agent**
    ```bash
    python main.py
    ```

## 🎥 Demo Logic
When you input a competition name (e.g., "Titanic"), the agent will:
1.  **Search** Kaggle to find the exact competition reference.
2.  **Download** the data files to a local folder.
3.  **Read** the `train.csv` file to find columns like `Survived`, `Age`, `Sex`.
4.  **Reason** that `Survived` is the target and `Sex` is categorical.
5.  **Write** a `submission.py` script that handles this logic and saves it to your disk.

## 🛠️ Built With
* Python
* Google Gemini API
* Kaggle API
