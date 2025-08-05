from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data
prices = pd.read_csv("analysis/change_points.csv")  # detected change points
events = pd.read_csv("analysis/events.csv")         # manually labeled events

@app.route("/api/price-change-points")
def get_change_points():
    return jsonify(prices.to_dict(orient="records"))

@app.route("/api/events")
def get_events():
    return jsonify(events.to_dict(orient="records"))

@app.route("/api/combined")
def get_combined():
    merged = pd.merge(prices, events, how='left', left_on='DetectedChangeDate', right_on='EventDate')
    return jsonify(merged.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
