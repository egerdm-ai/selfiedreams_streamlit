import requests
import json
import base64
import io
from PIL import Image
import re
import random
import string
#34.32.248.151
url = "https://fair-results-melt.loca.lt/text2img"  # your API endpoint

payload = {
  "prompt": "a vibrant portrait of kefe_clk transformed into a Disney character, with flowing hair, glowing eyes, colorful attire, magical background, magical powers,  digital painting, by renowned Disney concept artist captivating, attention to detail, expressive facial features –upbeta –upbeta",
  "negative_prompt": "bad quailty, disturbed",
  "scheduler": "EulerAncestralDiscreteScheduler",
  "image_height": 512,
  "image_width": 512,
  "num_images": 4,
  "guidance_scale": 7,
  "steps": 34,
  "seed": -1
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

# Printing the response


data = json.loads(response.text)
print(data)

# Get the image data
images = data["images"]

prompt = payload["prompt"]

# Search for the word after " as "
match = re.search(r' as (\w+)', prompt)

if match:
    # If a match is found, the word will be in the first group
    image_name = match.group(1)
else:
    # Generate a random word
    image_name = ''.join(random.choices(string.ascii_lowercase, k=5))  # Change 5 to the length of the word you want

print(f'image_name: {image_name}')
#image_name = "batman"

for i, base64_string in enumerate(images):
    # Decode the base64 string to bytes
    image_bytes = base64.b64decode(base64_string)

    # Convert bytes to a PIL image
    image = Image.open(io.BytesIO(image_bytes))

    # Save the image
    image.save(f"images/{image_name}_{i+1}.png")
    print("saved " + str(i+1) + " images")


