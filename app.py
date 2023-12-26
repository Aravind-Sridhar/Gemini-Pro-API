# Import the streamlit module and alias it as st
import streamlit as st

# Import the os module
import os

# Import the google.generativeai module and alias it as ga
import google.generativeai as ga

# Import the load_dotenv function from the dotenv module
from dotenv import load_dotenv

# Load environment variables from a .env file in the current directory
load_dotenv()

# Configure the generative AI module with the Google API key from the environment variables
ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model named 'gemini-pro'
model = ga.GenerativeModel('gemini-pro')

# Define a function to get a response from the Gemini Pro text generator
def get_gemini_pro(question):
    # Generate content using the question as input
    response = model.generate_content(question)

    # Return the text content of the response
    return response.text

# Set the page configuration for Streamlit with a specific title
st.set_page_config(
    page_title="Gemini Pro Model Text Generator",
)

# Display a header on the page
st.header('Gemini Pro Model Text Generator')

# Create a text input field labeled "Input" with a key "input"
ip = st.text_input("Input: ", key="input")

# Create a button labeled "Submit Query"
submit = st.button("Submit Query")

# Check if the button is clicked
if submit:
    # Get the response from the Gemini Pro text generator
    op = get_gemini_pro(ip)

    # Display a subheader for the generator output
    st.subheader("Gemini Pro Model Generator Output:")

    # Display the generated output
    st.write("Output: ", op)
