from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

@app.route('/e-trading', methods=['GET', 'POST'])
def e_trading():
    farmer_details = None
    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        price = request.form['price']
        seller = request.form['seller']
        contact = request.form['contact']
        farmer_details = {
            'product': product,
            'quantity': quantity,
            'price': price,
            'seller': seller,
            'contact': contact
        }
        # Do NOT redirect here! Render directly so details are available
        return render_template("e_trading.html", farmer_details=farmer_details)
    return render_template("e_trading.html")

# Crop prediction code (unchanged)
MODEL_PATH = os.path.join("model", "crop_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        features = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]
        pred = model.predict([features])[0]
        return jsonify({'crop': pred})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)