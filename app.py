import numpy as np
from flask import Flask,request, render_template, url_for
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from werkzeug.utils import secure_filename
from keras.preprocessing import image



app = Flask(__name__)
#model = keras.models.load_model('Covid_Vgg.h5')
@app.route("/")
def index():
    #return render_template('index.html')
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)
