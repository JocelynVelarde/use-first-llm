import streamlit as st

st.title("Welcome to my first LLM requests")

st.header("OpenAI API")
open_ai_prompt = st.text_input("Please type your prompt")
if st.button("Send"):
    # gpt method
    st.success("Content generated!")
else: 
    st.warning("Please insert a prompt")

st.divider()

st.header("Gemini API")
gemini_prompt = st.text_input("Please type your prompt")
gemini_tokens = st.number_input("Please select number of tokens")
if st.button("Send"):
    # gpt method
    st.success("Content generated!")
else: 
    st.warning("Please insert a prompt")