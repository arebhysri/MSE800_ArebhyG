from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder='templete')  # use existing folder name
# config
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
UPLOAD_SUBFOLDER = 'uploads'
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', UPLOAD_SUBFOLDER)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render home page with default image."""
    image_url = 'https://www.megawecare.com/_next/image?url=https%3A%2F%2Fcdn.megawecare.com%2FGHBY%2FFeatured-Images%2F1730956150973-Best_Outdoor_Games_For_Kids_876X400.webp&w=1920&q=75'
    return render_template('index.html', image_url=image_url)

@app.route('/upload', methods=['POST'])
def upload():
    """Handle image upload and display."""
    if 'image' not in request.files:
        """Handle missing file part."""
        return render_template('index.html', error='No file part', image_url=None)
    file = request.files['image']
    if file.filename == '':
        """Handle empty file upload."""
        return render_template('index.html', error='No selected file', image_url=None)
    if file and allowed_file(file.filename):
        """Save the uploaded image."""
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        uploaded_url = url_for('static', filename=f'{UPLOAD_SUBFOLDER}/{filename}')
        return render_template('index.html', image_url=uploaded_url)
    return render_template('index.html', error='File type not allowed', image_url=None)

if __name__ == '__main__':
    app.run(debug=True)