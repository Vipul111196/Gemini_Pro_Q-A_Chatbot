# Importing the required libraries
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Loading all the environment variables
load_dotenv() 

# Setting up the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

# Function to get the response from the Gemini model
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

# Initialize our streamlit app
st.set_page_config(page_title="Gemini Q&A Chatbot", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

st.header("Gemini Q&A Chatbot")

# Input section
input = st.text_input("Input:", key="input", placeholder="Enter your question here")
submit = st.button("Ask the question")

# Processing the response when the submit button is clicked
if submit and input:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
    



    

