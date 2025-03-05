from flask import Flask, render_template
import pymysql

app = Flask(__name__, template_folder='C:/cloud_migration_project/nginx/html/board')

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Global!23',
        database='bulletin_board',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM posts ORDER BY created_at DESC"
            cursor.execute(sql)
            posts = cursor.fetchall()
        return render_template('index.html', posts=posts)
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
