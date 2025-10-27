# FMPU: AI Image Compositor

**Event:** HackAI 2025  
**Languages and Tools:** Python · Stable Diffusion · rembg · Pillow · Torch

---

## Overview
FMPU (Fast Modular Photo Upgrader) is a Python-based image compositor that removes the background from an input image, generates a new background using Stable Diffusion v1-5, and merges them into a single composite image. Developed during HackAI 2025, this project explores creative applications of generative AI in image editing by combining computer vision and diffusion-based image synthesis.

---

## Features
- Removes image backgrounds using **rembg**, which applies AI-driven alpha matting  
- Generates new background images from text prompts using **Stable Diffusion v1-5**  
- Composes the processed foreground and AI-generated background with **Pillow** for seamless blending  
- Uses **Torch** for GPU-accelerated model inference and local processing  
- Handles common errors for missing files, invalid paths, and model initialization issues

---

## Technologies Used
- **Python**  
- **rembg**  
- **diffusers** (Stable Diffusion v1-5)  
- **Pillow (PIL)**  
- **Torch**

---

## Installation

1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/fmpu-ai-image-compositor.git
   cd fmpu-ai-image-compositor
   ```

2. Create and activate a virtual environment (optional but recommended)  
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS or Linux
   source .venv/bin/activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script  
   ```bash
   python FMPU.py
   ```

---

## Usage

1. Place your input image in the project directory (for example, `test_input.jpg`).  
2. When prompted, enter a text prompt for background generation (for example, "Ohio State Buckeyes").  
3. The script will:  
   - Generate a background from your prompt  
   - Remove the original background from the input image  
   - Composite the subject over the generated background  
   - Save the result to the specified output path  

**Example**  
- Input: `test_input.jpg`  
- Prompt: "Ohio State Buckeyes"  
- Output: `test_output.jpg`

---

## Project Structure
```
FMPU/
├── FMPU.py             # Main script
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## Key Functions
- `generate_background(prompt)`: Generates a background image from a text prompt using Stable Diffusion  
- `remove_bg(input_path)`: Removes the background from an input image using rembg  
- `compose_images(foreground, background)`: Overlays the foreground on the generated background for a composite output  
- `create_composite(input_image_path, background_prompt, output_path)`: Orchestrates the full pipeline of background generation, removal, and composition  

---

## Example Workflow
1. User provides an input image  
2. A text prompt is passed to the diffusion model to create a background  
3. rembg extracts the subject from the input image  
4. The foreground and generated background are composited  
5. The final PNG is written to disk  

---

## Skills and Concepts
Python Programming · Stable Diffusion · rembg · Pillow (PIL) · Torch · Diffusers · Image Processing · Computer Vision · Artificial Intelligence (AI) · Generative AI

---

## Results
Developed for HackAI 2025, FMPU demonstrates a modular approach to AI-assisted image editing and generation with local inference.

---

## License
This project is for educational and hackathon purposes only.
