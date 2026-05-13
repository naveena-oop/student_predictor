from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    attendance = float(request.form['attendance'])
    study_hours = float(request.form['study_hours'])
    prev_score = float(request.form['prev_score'])

    features = np.array([[attendance, study_hours, prev_score]])
    prediction = model.predict(features)[0]

    result = "✅ PASS" if prediction == 1 else "❌ FAIL"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)