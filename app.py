from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask is working with Anaconda!"

@app.route('/show')
def show():
    return "🚀 Route /show is working"

if __name__ == '__main__':
    app.run(debug=True)
