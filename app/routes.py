from flask import Flask, request, jsonify
from .database_manager import DatabaseManager
from flasgger import Swagger

app = Flask(__name__)

@app.route('/submitData', methods=['POST'])
def submit_data():
    """
    Добавление информации о перевале
    ---
    tags:
      - Перевалы
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Эльбрус
            height:
              type: integer
              example: 5642
            location:
              type: string
              example: Кавказ
            user_id:
              type: integer
              example: 1
    responses:
      201:
        description: Перевал успешно добавлен
    """
    data = request.json
    db_manager = DatabaseManager()
    db_manager.add_pass(data)
    db_manager.close()
    return jsonify({"status": "success", "message": "Pass added successfully"}), 201    