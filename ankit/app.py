#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    import pyttsx3
    engine = pyttsx3.init()
    text = request.form.get("plain-text")
    voice=engine.say(text)
    engine.runAndWait()
    return render_template('index.html',)

if __name__ == "__main__":
    app.run(debug=True)