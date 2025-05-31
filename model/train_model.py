import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os

# --------- PATHS ---------
DATA_PATH = "C:\\Users\\ms900\\OneDrive\\Desktop\\Smart_Crop_Prediction\\Crop_recommendation.csv"
MODEL_PATH = os.path.join("model", "crop_model.pkl")

# --------- LOAD DATA ---------
df = pd.read_csv(DATA_PATH)
print("First 5 rows of the data:")
print(df.head())

# --------- FEATURES & LABEL ---------
X = df.drop('label', axis=1)
y = df['label']

# --------- TRAIN/TEST SPLIT ---------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --------- MODEL TRAINING ----------
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# --------- EVALUATE ---------------
y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))

# --------- SAVE MODEL -------------
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump(clf, f)
print("Model saved to", MODEL_PATH)