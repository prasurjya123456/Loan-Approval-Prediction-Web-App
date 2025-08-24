from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load dataset
DATA_PATH = 'data.csv'
df = pd.read_csv(DATA_PATH)

# Load regression model and scaler
reg_model = joblib.load('reg_model.pkl')
scaler = joblib.load('scaler_reg.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            # Get form input
            requested_amount = float(request.form['requested_amount'])
            officer_score = float(request.form['officer_score'])
            processing_days = float(request.form['processing_days'])

            # Prepare input array and scale
            input_data = np.array([[requested_amount, officer_score, processing_days]])
            input_scaled = scaler.transform(input_data)

            # Make prediction
            prediction = reg_model.predict(input_scaled)[0]
            prediction = round(prediction, 2)
        except Exception as e:
            print("Error in prediction:", e)
            prediction = None

    # Convert the dataset to HTML
    data_html = df.to_html(classes='table', index=False)  # limit rows to 100

    return render_template('index.html', prediction=prediction, data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)
