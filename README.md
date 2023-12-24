# Gemini LLM Application

This project demonstrates a simple Q&A application using Google's Gemini Pro model integrated with a Streamlit web application. The app allows users to ask questions and receive responses from the Gemini language model in real-time.

## Features

- **Streamlit Interface**: An easy-to-use web interface built with Streamlit.
- **Google Gemini Pro**: Leverage the power of Google's Gemini Pro language model to generate responses to user queries.
- **Real-Time Interaction**: Users can interact with the model in real-time, receiving responses as they type.
- **Session-Based Chat History**: The application maintains a session-based chat history, allowing users to see previous queries and responses.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Vipul111196/Gemini_Pro_Q-A_Chatbot.git
    cd Gemini_Pro_Q-A_Chatbot
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root of the project.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your-google-api-key
      ```

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit application in your browser.
2. Enter your question in the text input field.
3. Click on the "Ask the question" button to send your query.
4. The response from the Gemini model will be displayed in real-time.
5. Previous interactions can be viewed in the chat history section.

## Project Structure

- `app.py`: The main script that runs the Streamlit application.
- `requirements.txt`: A list of Python dependencies required to run the application.
- `.env`: A file to store environment variables (not included in the repository for security reasons).

## Requirements

- Python 3.8 or higher
- Streamlit
- Python-dotenv
- Google's Generative AI Python Client Library

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.
