# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as ga

# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI module with the Google API key from the environment variables
ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model named 'gemini-pro' and start a chat session with an empty history
model = ga.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to get a response from the Gemini Pro chatbot given a question
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set up Streamlit page configuration
st.set_page_config(page_title="Gemini Pro Chatbot Interface")

# CSS styling for chat messages
chat_styles = """
    div[role="listbox"] > div:nth-child(odd) {
        background-color: #f1f1f1;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 5px;
    }
    div[role="listbox"] > div:nth-child(even) {
        background-color: #efffff;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 5px;
    }
"""

# Apply the custom CSS styling
st.markdown(f'<style>{chat_styles}</style>', unsafe_allow_html=True)

# Display the main title for the page
st.title("Gemini Pro Chatbot Interface")

# Check if 'chat_history' is not in the current session state
if 'chat_history' not in st.session_state:
    # If not, initialize 'chat_history' as an empty list in the session state
    st.session_state['chat_history'] = []

# Create a container for displaying the chat history
chat_container = st.container()

# Iterate over the chat history and display it in a chat-like format
with chat_container:
    st.subheader("Chat History")

    for role, text in st.session_state['chat_history']:
        if role == "User":
            # Display the user's input with a user-friendly style
            st.markdown(f'<div style="color: #264653; font-weight: bold;">{role}: {text}</div>', unsafe_allow_html=True)
        else:
            # Display the chatbot's response with a chatbot-friendly style
            st.markdown(f'<div style="color: #2a9d8f; font-weight: bold;">{role}: {text}</div>', unsafe_allow_html=True)

# Container for user input
input_container = st.container()

# Get user input and process it
with input_container:
    st.subheader("User Input")
    # Display a text input field for the user to enter input
    user_input = st.text_input("You:", key="user_input")
    # Display a button to submit the user input
    submit_button = st.button("Send")

# Process user input and get Gemini Pro's response
if submit_button and user_input:
    # Append the user's input to the chat history
    st.session_state['chat_history'].append(("User", user_input))
    # Get the response from Gemini Pro chatbot for the user input
    response = get_gemini_response(user_input)

    # Update the chat history with Gemini Pro's response
    with chat_container:
        st.subheader("Gemini Pro Response")
        for chunk in response:
            # Display each line of Gemini Pro's response separately in the chat history
            st.markdown(f'<div style="color: #2a9d8f; font-weight: bold;">Gemini Pro: {chunk.text}</div>', unsafe_allow_html=True)
            st.session_state['chat_history'].append(("Gemini Pro", chunk.text))
