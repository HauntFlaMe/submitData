import os
import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('FSTR_DB_HOST'),
            port=os.getenv('FSTR_DB_PORT'),
            dbname=os.getenv('FSTR_DB_NAME'),
            user=os.getenv('FSTR_DB_LOGIN'),
            password=os.getenv('FSTR_DB_PASS')
        )
        self.cursor = self.conn.cursor()

    def add_pass(self, pass_data):
        query = sql.SQL("""
            INSERT INTO passes (name, height, location, user_id, status)
            VALUES (%s, %s, %s, %s, 'new')
        """)
        self.cursor.execute(query, (
            pass_data['name'],
            pass_data['height'],
            pass_data['location'],
            pass_data['user_id']
        ))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
