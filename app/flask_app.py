from flask import Flask, render_template

app = Flask(__name__, template_folder='C:\cloud_migration_project\nginx\html\board')

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',          # 온프레미스 환경의 MySQL 서버 호스트
        user='root',               # 사용자 이름
        password='your_password',  # 비밀번호
        database='your_database',  # 데이터베이스 이름
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/api/posts', methods=['GET'])
def get_posts():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            results = cursor.fetchall()
        return jsonify(results)
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
