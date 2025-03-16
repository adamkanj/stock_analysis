from datetime import datetime, timedelta

import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# Generate Sample Data
def generate_sample_data():
    start_date = datetime.today() - timedelta(days=30)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    data = {
        "Date": [d.strftime("%Y-%m-%d") for d in dates],
        "Name": ["User " + str(i) for i in range(30)],
        "Amount": [round(100 + i * 5.5, 2) for i in range(30)],
    }
    return pd.DataFrame(data)


df = generate_sample_data()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/filter", methods=["POST"])
def filter_data():
    try:
        data = df.copy()
        req = request.get_json()
        start_date = req.get("start_date")
        end_date = req.get("end_date")

        if start_date and end_date:
            data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]

        return jsonify(data.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
