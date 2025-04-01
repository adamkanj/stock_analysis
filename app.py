from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Sample work order data (Simulating database)
work_orders = {
    1: {
        "work_order_number": "WO12345",
        "server_id": "SRV001",
        "code_blue": "YES",
        "scheduled_date": "2025-03-20",
        "escalate": False,
        "client_specialist": "Adam K.",
        "client_confirmed": "YES",
    },
    2: {
        "work_order_number": "WO67890",
        "server_id": "SRV002",
        "code_blue": "NO",
        "scheduled_date": "2025-03-22",
        "escalate": True,
        "client_specialist": "Sarah M.",
        "client_confirmed": "NA",
    },
}


@app.route("/")
def home():
    return render_template("index.html", work_orders=work_orders)


@app.route("/update_work_order", methods=["POST"])
def update_work_order():
    data = request.json
    work_order_id = int(data["id"])

    if work_order_id in work_orders:
        work_orders[work_order_id].update(data)
        return jsonify({"success": True, "message": "Work order updated successfully!"})
    else:
        return jsonify({"success": False, "message": "Work order not found!"})


if __name__ == "__main__":
    app.run(debug=True)
