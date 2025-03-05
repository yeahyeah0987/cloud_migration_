import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASS', ''),
        database=os.getenv('DB_NAME', 'bulletin_board'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM posts")
            rows = cursor.fetchall()
        return jsonify(rows)
    finally:
        conn.close()

if __name__ == '__main__':
    # 개발 환경에서 테스트 시
    app.run(host='0.0.0.0', port=8000, debug=True)
