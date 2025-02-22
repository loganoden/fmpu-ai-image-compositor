from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    """
    Remove background from an image and save the result
    
    Parameters:
    input_path (str): Path to input image
    output_path (str): Path where the output image will be saved
    """
    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the output image with transparent background
        output_image.save(output_path, format='PNG')
        print(f"Background removed successfully. Image saved at: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def process_directory(input_dir, output_dir):
    """
    Process all images in a directory
    
    Parameters:
    input_dir (str): Directory containing input images
    output_dir (str): Directory where processed images will be saved
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Supported image formats
    supported_formats = ['.png', '.jpg', '.jpeg']
    
    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(fmt) for fmt in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"nobg_{filename}")
            remove_background(input_path, output_path)

if __name__ == "__main__":
    # Example usage for a single image
    remove_background("test_input.jpg", "test_output.jpg")
    # Example usage for processing an entire directory
    # process_directory("input_folder", "output_folder")
