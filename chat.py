from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as ga


os.getenv("GOOGLE_API_KEY")
ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = ga.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):

    response = chat.send_message(question,  stream=True)

    return response

st.set_page_config(page_title="Gemini Pro Q&A Demo")

st.header("Gemini Pro Chat Application")

input = st.text_input("Input: ", key="input")


submit = st.button("Ask the question")

if submit:

    response = get_gemini_response(input)
    st.subheader("Gemini Pro Says")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)

    st.write(chat.history)