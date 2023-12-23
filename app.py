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


    



    

