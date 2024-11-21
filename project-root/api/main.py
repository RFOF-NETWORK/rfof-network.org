from flask import Flask, request, jsonify
from handlers import transaction_handler, token_handler, user_handler

app = Flask(__name__)

@app.route('/send-tokens', methods=['POST'])
def send_tokens():
    data = request.get_json()
    response = transaction_handler.handle_transaction(data)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
