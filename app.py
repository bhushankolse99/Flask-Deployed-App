import os
import logging
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import pandas as pd
import tensorflow as tf


logging.basicConfig(level=logging.DEBUG)

# Load disease and supplement information CSV files
disease_info = pd.read_csv('disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv', encoding='cp1252')



app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():    
    return render_template('submit.html')


@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', 
                           supplement_image=list(supplement_info['supplement image']),
                           supplement_name=list(supplement_info['supplement name']), 
                           disease=list(disease_info['disease_name']), 
                           buy=list(supplement_info['buy link']))

if __name__ == '__main__':
    app.run(debug=True)
