import numpy as np
from flask import Flask,request, render_template, url_for
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from werkzeug.utils import secure_filename
from keras.preprocessing import image



app = Flask(__name__)
model = keras.models.load_model('Covid_Vgg.h5')
@app.route("/index/")
def index():
    return render_template('index.html')
    return 'Hello, World!'

@app.route("/index/", methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.form['file']
        img = image.load_img(img, target_size=(150, 150))
        img = np.expand_dims(img, axis=0)
        predictions = model.predict_classes(img)
        print(predictions)
    return render_template('index.html', prediction=predictions)
if __name__ == '__main__':
    app.run(debug=True)