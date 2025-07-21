from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {}

@app.route('/')
def home():
    return "✅ Flask is running!"

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    latest_data = request.json
    return jsonify({"status": "✅ Received", "data": latest_data})

@app.route('/show', methods=['GET'])
def show():
    return jsonify(latest_data)
