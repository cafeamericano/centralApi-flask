# Imports
from flask import Flask, Blueprint, jsonify
import os

# Define app variable
app = Flask(__name__)

# Define port on which to listen
port = int(os.environ.get("PORT", 5000))

# Import route files
from apis.globeMonitor import GlobeMonitorAPI

# Register route files
app.register_blueprint(GlobeMonitorAPI)

# Root URL Route
@app.route('/')
def home():
    return '<h2>Centralized API - Flask</h2><p>Version 0.1</p><p>The server is listening for requests.</p>'

# Start server listening
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

