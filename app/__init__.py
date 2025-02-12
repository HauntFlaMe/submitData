from flask import Flask

app = Flask(__name__)

# Импортируем маршруты
from . import routes