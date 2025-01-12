# This file will serve as our GPT connection
from openai import OpenAI
import streamlit as st

api_key = st.secrets["api_key"]
client = OpenAI(api_key=api_key)

def generate_text(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)
print(response.data[0].url)