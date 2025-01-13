# This file will serve as our Gemini connection

import google.generativeai as genai
import streamlit as st

api_key = st.secrets["api_key_google"]

def generate_gemini_text(prompt, tokens):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
            max_output_tokens=tokens,
            temperature=0.1,
        )
    )
    return response.text