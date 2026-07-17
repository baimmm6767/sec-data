import os
from flask import Flask, request, jsonify, send_from_directory
import requests

# Set the static folder to the current directory
app = Flask(__name__, static_folder='.', static_url_path='')

# 1. The Proxy Route (handles the external API calls)
@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        resp = requests.get(url)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Serve the main index.html file
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# 3. Serve any other static files (CSS, JS, images) if you have them
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Run the combined server on port 8000
    print("Starting combined server at http://localhost:8000")
    app.run(port=8000)
