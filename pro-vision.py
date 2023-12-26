# Import the streamlit module and alias it as st
import streamlit as st

# Import the os module
import os

# Import the google.generativeai module and alias it as ga
import google.generativeai as ga

# Import the Image class from the PIL module
from PIL import Image

# Import the load_dotenv function from the dotenv module
from dotenv import load_dotenv

# Load environment variables from a .env file in the current directory
load_dotenv()

# Configure the generative AI module with the Google API key from the environment variables
ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model named 'gemini-pro-vision'
model = ga.GenerativeModel('gemini-pro-vision')

# Define a function to get a response from the Gemini Pro Vision generator
def get_gemini_pro_vision(input, image):
    # Create a generative model specifically for vision
    model = ga.GenerativeModel('gemini-pro-vision')

    # Check if input is provided, generate content with both input and image; otherwise, generate content only with the image
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)

    # Return the text content of the response
    return response.text

# Set the page configuration for Streamlit with a specific title
st.set_page_config(
    page_title="Gemini Pro Vision Generator",
)

# Display a header on the page
st.header('Gemini Pro Vision Generator')

# Create a text input field labeled "Input Prompt" with a key "input"
inp = st.text_input("Input Prompt: ", key="input")

# Create a file uploader component for choosing an image with accepted file types
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Initialize an empty string for the image
image = ""

# Check if an image is uploaded
if uploaded_file is not None:
    # Open the uploaded image using the PIL Image class
    image = Image.open(uploaded_file)

    # Display the uploaded image with a caption
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Create a button labeled "Tell me about the image"
submit = st.button("Tell me about the image")

# Check if the button is clicked
if submit:
    # Get the response from the Gemini Pro Vision generator
    response = get_gemini_pro_vision(inp, image)

    # Display a subheader for the response
    st.subheader("The Response is: ")

    # Display the response text
    st.write(response)
