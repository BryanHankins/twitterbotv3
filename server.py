from flask import Flask, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to your Flask server! 🚀"
    })

# Dynamic route example
@app.route('/hello/<name>')
def hello(name):
    return jsonify({
        "message": f"Hello, {name}! Welcome to the Flask server!"
    })

# Run the app
if __name__ == '__main__':
    # Use '0.0.0.0' to make the server accessible externally
    # Use a specific port (e.g., 5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
