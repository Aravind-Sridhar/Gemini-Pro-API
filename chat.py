# Import the load_dotenv function from the dotenv module
from dotenv import load_dotenv

# Load environment variables from a .env file in the current directory
load_dotenv()

# Import the streamlit module and alias it as st
import streamlit as st

# Import the os module
import os

# Import the google.generativeai module and alias it as ga
import google.generativeai as ga

# Get the value of the "GOOGLE_API_KEY" environment variable
os.getenv("GOOGLE_API_KEY")

# Configure the generative AI module with the Google API key from the environment variables
ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model named 'gemini-pro' and start a chat session with an empty history
model = ga.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Define a function to get a response from the Gemini Pro chatbot given a question
def get_gemini_response(question):
    # Send the question to the chatbot and get the response
    response = chat.send_message(question, stream=True)
    return response

# Set the page configuration for Streamlit with a specific title
st.set_page_config(page_title="Gemini Pro Q&A Demo")

# Display a header on the page
st.header("Gemini Pro Chat Application")

# Create a text input field labeled "Input" with a key "input"
input = st.text_input("Input: ", key="input")

# Create a button labeled "Ask the question"
submit = st.button("Ask the question")

# Check if the button is clicked
if submit:
    # Get the response from Gemini Pro chatbot for the input
    response = get_gemini_response(input)

    # Display a subheader for Gemini Pro's response
    st.subheader("Gemini Pro Says")

    # Iterate over the response chunks and display them
    for chunk in response:
        # Print each chunk of the response and a separator line
        print(st.write(chunk.text))
        print("_" * 80)

    # Display the chat history
    st.write(chat.history)
