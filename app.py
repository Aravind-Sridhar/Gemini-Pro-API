import streamlit as st
import os
import google.generativeai as ga

from dotenv import load_dotenv

load_dotenv()

ga.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = ga.GenerativeModel('gemini-pro')

def get_gemini_pro(question):

    response = model.generate_content(question)

    return response.text


st.set_page_config(
    page_title="Gemini Pro Model Text Generator",
)

st.header('Gemini Pro Model Text Generator')

ip = st.text_input("Input: ", key="input")
submit = st.button("Submit Query")

if submit:
    op = get_gemini_pro(ip)
    st.subheader("Gemini Pro Model Generator Output:")
    st.write("Output: ", op)
