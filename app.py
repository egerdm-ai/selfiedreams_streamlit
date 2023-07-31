import streamlit as st
import requests
import json
import base64
import io
from PIL import Image
import re
import random
import string

# Function to call the API and return the response
def call_api(prompt):
    url = "https://slick-stars-do.loca.lt/text2img"  # your API endpoint
    payload = {
      "prompt": prompt,
      "negative_prompt": "bad quailty, disturbed",
      "scheduler": "EulerAncestralDiscreteScheduler",
      "image_height": 512,
      "image_width": 512,
      "num_images": 4,
      "guidance_scale": 7,
      "steps": 34,
      "seed": -1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    data = json.loads(response.text)
    return data

# Streamlit App
st.title('AI Image Generator')

# User input
prompt = st.text_input('Enter your prompt:', 'a vibrant portrait of alicem_seker transformed into a Disney character')

if st.button('Generate'):
    # Get the images from the API
    data = call_api(prompt)
    images = data["images"]

    # Search for the word after " as "
    match = re.search(r' as (\w+)', prompt)

    if match:
        # If a match is found, the word will be in the first group
        image_name = match.group(1)
    else:
        # Generate a random word
        image_name = ''.join(random.choices(string.ascii_lowercase, k=5))  # Change 5 to the length of the word you want

    st.write(f'image_name: {image_name}')

    for i, base64_string in enumerate(images):
        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(base64_string)

        # Convert bytes to a PIL image
        image = Image.open(io.BytesIO(image_bytes))

        # Display the image
        st.image(image, caption=f"{image_name}_{i+1}.png", use_column_width=True)
