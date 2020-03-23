# Imports
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
import os

# Define app variable
app = Flask(__name__)

# Allow cross origin requests
CORS(app)

# Define port on which to listen
port = int(os.environ.get("PORT", 5000))

# Import route files
from apis.appGalleryLite import AppGalleryLiteAPI

# Register route files
app.register_blueprint(AppGalleryLiteAPI)

# Root URL Route
@app.route('/')
def home():
    return '<h2>Centralized API - Flask</h2><p>Version 1.0</p><p>The server is listening for requests.</p>'

# Start server listening
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

