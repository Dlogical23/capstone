import requests

# API URL (assuming running locally)
API_URL = "http://127.0.0.1:8000/predict/"

print("\nWelcome to the KMeans Cluster Predictor!")

while True:
    user_input = input("\nEnter feature values separated by commas (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        # Convert input string to list of floats
        feature_values = list(map(float, user_input.split(",")))
        response = requests.post(API_URL, json=feature_values)

        # Display cluster prediction
        print("📌 Cluster Prediction:", response.json())
    except Exception as e:
        print("❌ Error:", e)
