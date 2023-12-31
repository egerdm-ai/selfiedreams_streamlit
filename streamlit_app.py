import streamlit as st
import requests
import json
import base64
import io
from PIL import Image
import re
import pandas as pd
from io import BytesIO

# Function to call the API and return the response
def call_api(prompt,url):
    #url = url #"https://tasty-rings-wear.loca.lt/text2img"  # your API endpoint
    payload = {
      "prompt": prompt,
      "negative_prompt": "((((open mouth)))), ((((visible hand)))), ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck)))",
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

# Use markdown to center text# Use markdown to center text


st.markdown("<h1 style='text-align: center; color: #c770f0;'>AIi Cemerator</h1>", unsafe_allow_html=True)

left_column, main_column, right_column = st.columns([5,5,5])
img = Image.open('app_images/ali.jpg')
new_width = 256
new_height = int(new_width * img.height / img.width)
image0 = img.resize((new_width, new_height))

# Convert the image to a base64 string
buffered = BytesIO()
image0.save(buffered, format="JPEG")
image_base64 = base64.b64encode(buffered.getvalue()).decode()

# Display the image in a center-aligned markdown string
st.markdown(
    f'<p align="center"><img src="data:image/jpeg;base64,{image_base64}" /></p>', 
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center;'>Try the AI model that can generate images of Ali Cem!</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>You have to mention him as 'alicem_seker' 🙃</p>", unsafe_allow_html=True)

# Add two columns (the left one for the text input and the right one for the button)
left_column, right_column = st.columns([4,1])



# Use the left_column for the text input
prompt = left_column.text_input('Enter your prompt:', 'a selfie of alicem_seker with Rihanna')
st.markdown("""
<style>
    .stButton>button {
        color: white;
        background-color: #c770f0;
        height:2.8em; 
        width:6em; 
        font-size:1.5em;
    }
    .stButton>button:hover {
        color: white;
        border: 2px solid white;
    }
    .stButton>button:focused {
        color: white;
        background-color: #c770f0;
        border: 2px solid white;
    }
    .stButton>button:active {
        color: white;
        background-color: #c770f0;
        border: 2px solid white;
    }
    /* Center the button on screens smaller than 600px */
    @media (max-width: 600px) {
        .stButton>button {
            display: block;
            margin: 0 auto;
        }
    }
</style>
""", unsafe_allow_html=True)

# Use the right_column for the button
button = right_column.button('Generate')
# Load images
image1 = Image.open('app_images/batman_2.png')
image2 = Image.open('app_images/snoop.png')
image3 = Image.open('app_images/beyonce.jpeg')
image4 = Image.open('app_images/dungeon_master.png')

# Add three columns (the middle one is the main one)
left_column_0, main_column_0, right_column_0 = st.columns([2,1,2])
left_column_1, main_column_1, right_column_1 = st.columns([1,6,1])
left_column_2, main_column_2, right_column_2 = st.columns([1,6,1])
left_column_3, main_column_3, right_column_3 = st.columns([1,6,1])
left_column_4, main_column_4, right_column_4 = st.columns([1,6,1])

holder1 = main_column_1.empty()
holder2 = main_column_1.empty()
holder3 = main_column_1.empty()
holder4 = main_column_1.empty()

holder1.image(image2,caption ='a selfie of alicem_seker person with Snoop Dogg')
holder2.image(image3,caption ='a selfie of alicem_seker person with Beyonce')
holder3.image(image4,caption ='a portrait of alicem_seker person as a Dungeon Master')
holder4.image(image1,caption ='a black and white photo of alicem_seker')

if button:
    holder1.empty()
    holder2.empty()
    holder3.empty()
    holder4.empty()

    with st.spinner('Loading...'):
        # Get the images from the API
        url = st.secrets["url"]#"https://evil-moments-cheer.loca.lt/text2img"
        
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
            left_column, main_column, right_column = st.columns([1,6,1])
            main_column.image(image, use_column_width=True)
