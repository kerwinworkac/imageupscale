from flask import Flask, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from image_upscaler import upscale_images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        images = request.files.getlist('images')
        upscale_ratio = int(request.form['upscale-ratio'])

        if not images:
            return jsonify({'error': 'No images provided.'}), 400
        
        filenames = []
        for image in images:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)

        upscaled_images = upscale_images(filenames, upscale_ratio)
        return jsonify({'upscaled_images': upscaled_images})

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)