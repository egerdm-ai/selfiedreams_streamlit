import streamlit as st
import requests
import json
import base64
import io
from PIL import Image
import re
import pandas as pd

# Function to call the API and return the response
def call_api(prompt,url):
    url = "https://tasty-rings-wear.loca.lt/text2img"  # your API endpoint
    payload = {
      "prompt": prompt,
      "negative_prompt": "((((open mouth)))), ((((disturbed eyes)))), ((((ugly eyes)))), ((((visible hand)))), ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck)))",
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
st.title('AIi Cemerator')
st.subheader('Try the AI model that can generate images of Ali Cem!')
st.text('You have to mention him as "alicem_seker" 🙃')
# User input
#url = st.text_input('API URL:', '/text2img')
prompt = st.text_input('Enter your prompt:', 'a selfie of alicem_seker with Rihanna')

if st.button('Generate'):
    # Get the images from the API
    data = call_api(prompt,url)
    images = data["images"]

    # Search for the word after " as "
    match = re.search(r' as (\w+)', prompt)

    for i, base64_string in enumerate(images):
        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(base64_string)

        # Convert bytes to a PIL image
        image = Image.open(io.BytesIO(image_bytes))

        # Display the image
        st.image(image, use_column_width=True)
        
image1 = Image.open('app_images/batman_2.png')
image2 = Image.open('app_images/snoop.png')
image3 = Image.open('app_images/beyonce.jpeg')
image4 = Image.open('app_images/dungeon_master.png')

st.image(image2,caption ='a selfie of alicem_seker person with Snoop Dogg')
st.image(image3,caption ='a selfie of alicem_seker person with Beyonce')
st.image(image4,caption ='a portrait of alicem_seker person as a Dungeon Master')
st.image(image1,caption ='a black and white photo of alicem_seker')
