import os
import tensorflow as tf
import numpy as np 
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template, render_template_string, jsonify
from werkzeug.utils import secure_filename
from keras.preprocessing.image import load_img, img_to_array
app = Flask(__name__)

model = load_model(r'C:\Users\gowda\OneDrive\Desktop\python project 2.0\plant_disease_detection\model.h5')
print('Model loaded. Check http://127.0.0.1:5000/')

# Update this dictionary to match your model's class order
labels = {0: 'Healthy', 1: 'Powdery', 2: 'Rust'}


def getResult(image_path):
    img = load_img(image_path, target_size=(225,225))
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)[0]
    print("Predictions:", predictions)  # Debug print
    return predictions

# Map each label to a fruit name
fruit_names = {
    'Healthy': 'Apple',
    'Powdery': 'Apple',
    'Rust': 'Apple'
}

# Disease control recommendations
recommendations = {
    'Healthy': 'No disease detected. Maintain regular care.',
    'Powdery': 'Apply sulfur-based fungicides and remove infected leaves.',
    'Rust': 'Remove infected leaves and use appropriate fungicides.'
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
             basepath, 'uploads',secure_filename(f.filename))
        f.save(file_path)
        predictions = getResult(file_path)
        predicted_labels = labels [np.argmax(predictions)]
        return str(predicted_labels)
    return None


if __name__ == '__main__':
    app.run(debug=True)