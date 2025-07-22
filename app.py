from flask import Flask, request, jsonify, render_template_string

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

@app.route('/show_json', methods=['GET'])
def show_json():
    return jsonify(latest_data)

@app.route('/show', methods=['GET'])
def show_html():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Live LTP</title>
        <script>
            setTimeout(function(){
               window.location.reload(1);
            }, 60000);  // 60000 ms = 60 seconds
        </script>
    </head>
    <body>
        <h1>📈 Live Nifty & BankNifty LTP</h1>
        <pre>{{ data }}</pre>
    </body>
    </html>
    """
    return render_template_string(html_template, data=latest_data)
