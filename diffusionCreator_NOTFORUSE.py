from diffusers import StableDiffusionPipeline
import torch
import requests

# Load the pre-trained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4-original", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # If you have a GPU, else remove this line.

# Define the prompt for image generation
prompt = "a futuristic city skyline at sunset with flying cars"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image to the directory
image.save("generated_image.png")

print("Image generated and saved successfully!")
