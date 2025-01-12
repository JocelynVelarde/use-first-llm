# This file will serve as our GPT connection
from openai import OpenAI
import streamlit as st

api_key = st.secrets["api_key"]
client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
print(completion.choices[0].message.content)
