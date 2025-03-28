from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Willkommen bei der RFOF Network API!")

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
