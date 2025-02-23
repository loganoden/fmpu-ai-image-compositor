from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO
from FMPU import fmpu

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Python Web App!"

# Endpoint to process the image sent from the frontend
@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Get the base64 image from the request
        data = request.json.get('image')
        
        # Decode the base64 string into image data
        img_data = base64.b64decode(data.split(',')[1])
        
        # Open the image with PIL (Python Imaging Library)
        image = Image.open(BytesIO(img_data))
        
        #run fmpu on this image
        processed_image = fmpu(image, "Ohio State Buckeyes")
        
        # Save the processed image to a file (for demo purposes)
        processed_image.save('processed_image.png')

        # Convert the processed image back to base64 to send to frontend
        buffered = BytesIO()
        processed_image.save(buffered, format="PNG")
        processed_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        # Return the processed image as a data URL
        return jsonify({
            'processed_image_url': 'data:image/png;base64,' + processed_image_base64
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)