# FMPU: AI Image Compositor

**Event:** HackAI 2025  
**Languages and Tools:** Python · Stable Diffusion · rembg · Pillow · Torch  

---

## 📄 Overview
**FMPU** (Fast Modular Photo Upgrader) is a Python-based image compositor that removes the background from an input image, generates a new background using **Stable Diffusion v1-5**, and merges them into a single composite image.  

The project was developed during **HackAI 2025** to explore creative applications of generative AI in image editing and personalization.

---

## ⚙️ Features
- Removes image backgrounds using **rembg** (deep learning–based alpha matting)  
- Generates new background images from text prompts using **Stable Diffusion v1-5**  
- Composes foreground and background using **Pillow**, ensuring high-resolution blending  
- Includes exception handling for file paths, missing inputs, and inference errors  

---

## 🧠 Technologies Used
- **Python** – core development language  
- **rembg** – deep learning–based background removal  
- **diffusers (Stable Diffusion v1-5)** – background generation  
- **Pillow (PIL)** – image processing and composition  
- **Torch** – model inference backend  

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/fmpu-ai-image-compositor.git
   cd fmpu-ai-image-compositor
