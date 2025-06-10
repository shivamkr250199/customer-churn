from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and encoders
with open('model/best_random_forest_model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    model = model_data['model']
    feature_names = model_data['feature_name']

with open('model/encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = []
    for feature in feature_names:
        value = request.form[feature]
        # Encode categorical values if encoder exists
        if feature in encoders:
            value = encoders[feature].transform([value])[0]
        else:
            value = float(value)
        input_data.append(value)

    prediction = model.predict([input_data])[0]
    result = 'Churn' if prediction == 1 else 'No Churn'
    return render_template('result.html', result=result)

if __name__ == '__main__':
   app.run(debug=True)


