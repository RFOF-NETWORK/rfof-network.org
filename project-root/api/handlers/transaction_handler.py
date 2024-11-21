def handle_transaction(data):
    # Logik zur Handhabung von Transaktionen
    to = data.get('to')
    amount = data.get('amount')
    # Implementiere Token-Transfer-Logik hier
    return {"status": "success", "message": "Tokens sent successfully"}
