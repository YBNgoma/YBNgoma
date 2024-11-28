from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'

# Ensure upload and compressed directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_image():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    compression_ratio = float(request.form.get('compression_ratio', 1))
    if not (0 < compression_ratio <= 1):
        return "Invalid compression ratio. Use a value between 0 and 1.", 400

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Compress the image
        img = Image.open(file_path)
        compressed_path = os.path.join(COMPRESSED_FOLDER, f"compressed_{file.filename}")
        img.save(compressed_path, optimize=True, quality=int(compression_ratio * 100))

        # Serve the compressed file as a download
        return send_file(
            io.BytesIO(open(compressed_path, 'rb').read()),
            as_attachment=True,
            download_name=f"compressed_{file.filename}",
            mimetype='image/jpeg'
        )

if __name__ == '__main__':
    app.run(debug=True)
