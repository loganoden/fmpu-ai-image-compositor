# FMPU

A Python-based image modification software, developed for Hack AI 2025.

## Features

- Removes backgrounds from images using deep learning
- Supports common image formats (PNG, JPG, JPEG)
- Preserves transparency in output images
- Can process both single images and entire directories

## Prerequisites

Before running this project, make sure you have Python installed on your system. This project was developed with Python 3.x.

## Installation

1. Clone this repository or download the source code.

2. Install the required dependencies using pip:
```bash
pip install rembg
pip install Pillow
pip install onnxruntime
```

## Project Structure

```
background-remover/
│
├── remove_background.py    # Main script for background removal
├── README.md              # Project documentation
└── requirements.txt       # List of Python dependencies
```

## Dependencies

- `rembg`: For background removal using deep learning
- `Pillow`: For image processing
- `onnxruntime`: Required by rembg for model inference
- `numpy`: Required for image manipulation
- `python-opencv` (optional): For alternative implementation

## Troubleshooting

Common issues and their solutions:

1. **File Not Found Error**:
   - Ensure the input image is in the same directory as the script
   - Check if the filename matches exactly (case-sensitive)
   - Verify you're running the script from the correct directory

2. **Module Not Found Errors**:
   - Make sure all required packages are installed using pip
   - If using a virtual environment, ensure it's activated

## Contributing

This project was created for Hack AI 2025.
