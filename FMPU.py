from PIL import Image
from rembg import remove
from diffusers import DiffusionPipeline
import torch
import os

def generate_background(prompt):
    """
    Generate a background image using Stable Diffusion
    """
    try:
        pipeline = DiffusionPipeline.from_pretrained(
            "stable-diffusion-v1-5/stable-diffusion-v1-5", 
            torch_dtype=torch.float16
        )
        pipeline.to("cuda")
        result = pipeline(prompt).images[0]
        return result
    except Exception as e:
        print(f"Error generating background: {str(e)}")
        return None

def remove_bg(input_path):
    """
    Remove background from input image
    """
    try:
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' not found!")
            return None
            
        input_image = Image.open(input_path)
        return remove(input_image)
    except Exception as e:
        print(f"Error removing background: {str(e)}")
        return None

def compose_images(foreground, background):
    """
    Overlay foreground on background, matching sizes
    """
    try:
        # Resize background to match foreground size
        background = background.resize(foreground.size, Image.Resampling.LANCZOS)
            
        # Compose the images
        return Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))
    except Exception as e:
        print(f"Error composing images: {str(e)}")
        return None

def create_composite(input_image_path, background_prompt, output_path):
    """
    Main function to create the composite image
    """
    try:
        # Generate background
        print("Generating background image...")
        background = generate_background(background_prompt)
        if background is None:
            return
            
        # Remove background from input image
        print("Removing background from input image...")
        foreground = remove_bg(input_image_path)
        if foreground is None:
            return
            
        # Compose images
        print("Creating composite image...")
        result = compose_images(foreground, background)
        if result is None:
            return
            
        # Save result
        result.save(output_path, format='PNG')
        print(f"Composite image saved successfully at: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_image = "test_input.jpg"  # Your input image with subject
    background_prompt = "Ohio State Buckeyes"  # Customize background prompt
    output_image = "test_output.jpg" # Output image
    
    create_composite(input_image, background_prompt, output_image)
