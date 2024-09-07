from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from db1 import get_transactions,get_user_settings,update_user_settings
app = Flask(__name__)
CORS(app)





@app.route('/get_user_settings', methods=['GET'])
def get_user_settings_api():
    telegram_id = request.args.get('telegram_id')
    if not telegram_id:
        return jsonify({"error": "telegram_id is required"}), 400
    
    settings = get_user_settings(telegram_id)
    if settings:
        return jsonify(settings)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/get_transactions', methods=['GET'])
def get_transactions_api():
    transactions = get_transactions()
    return jsonify(transactions)



@app.route('/update_user_settings', methods=['POST'])
def update_user_settings_api():
    data = request.json
    telegram_id = data.get('telegram_id')
    settings = data.get('settings')
    
    if not telegram_id or not settings:
        return jsonify({"error": "telegram_id and settings are required"}), 400
    
    update_user_settings(telegram_id, settings)
    return jsonify({"message": "User settings updated successfully"})



if __name__ == '__main__':
    app.run(debug=True)