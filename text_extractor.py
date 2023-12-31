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
def get_gemini_pro_vision_text_extractor(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Define a function to process the input image for further use
def process_input_image(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Create a list with image information including MIME type and data
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set the page configuration for Streamlit with a specific title
st.set_page_config(
    page_title="Gemini Pro Text Extractor",
)

# Display a header on the page
st.header('Gemini Pro Text Extractor',)

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
submit = st.button("Tell me about the provided invoice")

# Define an input prompt for the generative model
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# Check if the submit button is clicked
if submit:
    # Process the uploaded image and get the generative model response
    image_data = process_input_image(uploaded_file)
    response = get_gemini_pro_vision_text_extractor(input_prompt, image_data, inp)

    # Display the response as a subheader and text
    st.subheader("Gemini Pro says: ")
    st.write(response)
