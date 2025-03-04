from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and results
model = joblib.load("kmeans_model.pkl")
import os
import pandas as pd

csv_path = "/app/model_results.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"❌ Error: '{csv_path}' not found inside the container.")

results_df = pd.read_csv(csv_path)

print("✅ File loaded successfully!")

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = pd.DataFrame([data["features"]])  # Convert input to DataFrame
    prediction = model.predict(features).tolist()
    return jsonify({"prediction": prediction})

@app.route("/results", methods=["GET"])
def get_results():
    return results_df.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
