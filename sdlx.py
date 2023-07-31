from diffusers import DiffusionPipeline, StableDiffusionXLImg2ImgPipeline
import torch
import re
import random

import string
model = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = DiffusionPipeline.from_pretrained(
    model,
    torch_dtype=torch.float16
)
pipe.to("cuda")
pipe.load_lora_weights("egerdm/sdlx_dreambooth", weight_name="pytorch_lora_weights.safetensors")


prompt = "portrait of ege19rdm by mario testino 1950, 1950s style, taken in 1950, detailed face of ege19rdm, sony a7r"
match = re.search(r' as (\w+)', prompt)

if match:
    # If a match is found, the word will be in the first group
    image_name = match.group(1)
else:
    # Generate a random word
    image_name = ''.join(random.choices(string.ascii_lowercase, k=5))

print(image_name)
for seed in range(5):
    generator = torch.Generator("cuda").manual_seed(seed)
    image = pipe(prompt=prompt, generator=generator, num_inference_steps=24, height = 512, width = 512)
    img = image.images[0]
    img.save(f"image2/{image_name}_{seed}.png")
