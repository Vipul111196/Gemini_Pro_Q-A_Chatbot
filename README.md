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