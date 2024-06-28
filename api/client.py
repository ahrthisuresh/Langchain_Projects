import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# def get_codellama_response(input_text):
#     response = requests.post("http://localhost:8000/essay/invoke",
#     json = {'input':{'topic':input_text}} )

#     return response.json()['output']

# def get_Ollama_response(input_text):
#     response = requests.post("http://localhost:8000/poem/invoke",
#     json = {'input':{'topic':input_text}} )

#     return response.json()['output']


def get_codellama_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


st.title("Langchain demo with two ollama apis")
input_text = st.text_input("Write an essay on:")
input_text1 = st.text_input("write an poem on:")

if input_text:
    st.write(get_codellama_response(input_text))
if input_text1:
    st.write(get_ollama_response(input_text1))

