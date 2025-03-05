# Flask + MySQL 게시판 예시

이 프로젝트는 Flask, MySQL, Nginx를 활용한 간단한 게시판 예시입니다.

## 폴더 구조
/ (루트)
├── app/
│   ├── flask_app.py         # Flask 애플리케이션 코드
│   ├── __init__.py          # (필요한 경우) 초기화 파일
│   └── requirements.txt     # 필요한 Python 패키지 목록
├── config/
│   └── nginx.conf           # Nginx 서버 설정 파일
├── scripts/
│   └── create_tables.sql    # MySQL 데이터베이스 및 테이블 생성 스크립트
├── public/
│   └── index.html           # 기본 HTML 파일 (필요 시 CSS, JS 등도 포함)
└── README.md                # 프로젝트 설명 문서


## 설정 및 실행 방법

1. Python 패키지 설치
   ```bash
   cd app
   pip3 install -r requirements.txt

2. MySQL 데이터베이스 구성
mysql -u root -p
source scripts/create_tables.sql;

3. 환경 변수 설정
export DB_HOST=localhost
export DB_USER=root
export DB_PASS=비밀번호
export DB_NAME=bulletin_board

4. Flask 애플리케이션 실행 (개발용)
cd app
python3 flask_app.py

5. Gunicorn + Nginx (운영용)
Gunicorn 실행
gunicorn --bind 127.0.0.1:8000 flask_app:app

Nginx 설정
/etc/nginx/sites-available/에 nginx.conf를 복사하고 심볼릭 링크 생성 후
sudo nginx -t
sudo systemctl reload nginx

