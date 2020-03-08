# Imports
from flask import Flask, Blueprint, jsonify

# Define app variable
app = Flask(__name__)

# Import route files
from apis.globeMonitor import GlobeMonitorAPI

# Register route files
app.register_blueprint(GlobeMonitorAPI)

# Root URL Route
@app.route('/')
def hello_whale():
    return '<h2>Centralized API - Flask</h2><p>Version 0.1</p><p>The server is listening for requests.</p>'

# Start server listening
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
