# Smart Crop Prediction and E-Trading Platform

Smart Crop Prediction and E-Trading Platform is an integrated web application designed to empower farmers by leveraging machine learning for crop recommendations and providing an online marketplace to sell their harvest directly to buyers. This platform bridges the gap between technology and agriculture, enabling data-driven decisions and transparent trading.

---

## 🚀 Features

### 🌱 Crop Prediction
- **Smart Recommendations:** Suggests optimal crops for sowing based on user-provided soil parameters and weather data.
- **Machine Learning Model:** Utilizes a trained ML model for accurate crop prediction.
- **User-Friendly Form:** Simple input form for farmers to enter soil nutrients (N, P, K), temperature, humidity, pH, and rainfall.

### 🛒 E-Trading Platform
- **Sell Your Harvest:** Farmers can list their freshly harvested products for sale.
- **Product Details:** Enter crop name, quantity, price per kg, seller name, and contact number.
- **Attractive UI:** A clean, modern interface with a blurred background image of a supermarket for a professional look.
- **Buyer Discovery:** Buyers can view available products and contact sellers directly.

---

## 🧠 Machine Learning Approach

The crop recommendation system uses a **Random Forest Classifier** trained on a dataset containing soil nutrients, pH, rainfall, temperature, and humidity.  
Random Forest is chosen for its accuracy, robustness, and ability to handle nonlinear relationships.

**Workflow:**
1. User enters soil/environmental parameters.
2. Model predicts the best crop to grow.
3. Result is displayed instantly.

---

## 🛒 E-Trading Portal

Farmers can:
- List their fresh produce with details (product name, quantity, price, contact info).
- Reach buyers directly, eliminating middlemen.

Buyers can:
- Browse available products.
- Contact sellers for purchase.

-----

## 📷 Screenshot

### First Page

![Screenshot 2025-06-01 030956](https://github.com/user-attachments/assets/ca21c285-6840-4f22-84fd-b9daba7f92f6)

### After enter the details

![Screenshot 2025-06-01 031106](https://github.com/user-attachments/assets/8e50d6a0-6db2-4628-b197-e7c46876e7e3)

### E-Trading Page

![Screenshot 2025-06-01 041035](https://github.com/user-attachments/assets/ac79c192-058c-4795-960c-94998df28e86)

### Enter the details

![Screenshot 2025-06-01 041141](https://github.com/user-attachments/assets/2f36b7d0-2e26-483f-8d91-789abaf1bedf)

### After posted

![Screenshot 2025-06-01 041306](https://github.com/user-attachments/assets/06dc92bf-389f-4d97-b512-e1f1520acfda)




---

## 🏗️ Project Structure

```
Smart_Crop_Prediction/
│
├── static/
│   └── style.css           # Main CSS for UI styling
├── templates/
│   ├── index.html          # Crop prediction form and result
│   └── e_trading.html      # E-trading/sell page
├── model/
│   └── crop_prediction.pkl # Trained ML model (if applicable)
├── app.py                  # Main Flask (or Django) application
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/muniasamyk/Smart_Crop_Prediction.git
cd Smart_Crop_Prediction
```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Application

```sh
python app.py
```

Open your browser and navigate to `http://localhost:5000`.

---

## ✨ Usage

### Crop Prediction
1. On the homepage, fill in the required field values (N, P, K, temperature, humidity, pH, rainfall).
2. Click **Predict Crop**.
3. The ML model
