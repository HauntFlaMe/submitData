from flask import Flask, request, jsonify
from .database_manager import DatabaseManager

app = Flask(__name__)

@app.route('/submitData', methods=['POST'])
def submit_data():
    data = request.json
    db_manager = DatabaseManager()
    db_manager.add_pass(data)
    db_manager.close()
    return jsonify({"status": "success", "message": "Pass added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)