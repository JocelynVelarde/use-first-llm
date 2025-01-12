# This file will serve as our GPT connection
from openai import OpenAI
import streamlit as st
import requests

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

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    image_response = requests.get(image_url)

    with open("otter.png", 'wb') as file:
        file.write(image_response.content)