![Chatbot demo](https://github.com/Aravind-Sridhar/Gemini-Pro-API/blob/master/gemini.jpeg)

# Gemini Pro Demos

This repository contains multiple demos showcasing the capabilities of the Gemini Pro models using Streamlit. Below are brief descriptions and instructions for each demo.

## Getting Started

### Prerequisites

- Python >= 3.9
- [Streamlit](https://streamlit.io/)
- [Google GenerativeAI](https://cloud.google.com/ai-platform/generative-ai)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aravind-Sridhar/Gemini-Pro-API.git
   ```


2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the project directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your-api-key
   ```

   Replace `your-api-key` with your actual Google API key.


### 1. Gemini Pro Chat Interface

This is a Streamlit web application for interacting with the Gemini Pro chatbot. Users can input text, and the chatbot responds accordingly. The chat history is displayed in a chat-like format on the page.

### Usage

1. Run the Streamlit app:

   ```bash
   streamlit run gemini_pro_chat_interface.py
   ```

2. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).

3. Interact with the Gemini Pro chatbot by entering text in the input field and clicking the "Send" button.

## Features

- Chat history displayed in a visually appealing chat-like interface.
- User-friendly and chatbot-friendly message styling.
- Real-time updates as the user interacts with the chatbot.

## Customization

Feel free to customize the code to suit your preferences and requirements. You can adjust the CSS styling, add more features, or integrate additional functionalities.



### 2. Gemini Pro Vision Generator

This demo allows users to provide an input prompt and upload an image to generate content using the Gemini Pro Vision model.

#### Usage

1. Run the Streamlit app:

    ```bash
    streamlit run pro-vision.py
    ```

4. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).

5. Interact with the Gemini Pro Vision generator by entering an input prompt, uploading an image, and clicking the "Tell me about the image" button.

