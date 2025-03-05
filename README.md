# Flask + MySQL 게시판 예시

이 프로젝트는 **Flask**, **MySQL**, **Nginx**를 활용한 간단한 게시판 예시입니다.

## 폴더 구조

```
/ (루트)
├── app/
│   ├── flask_app.py       # Flask 애플리케이션 코드
│   ├── __init__.py        # (필요 시) 초기화 파일
│   └── requirements.txt   # 필요한 Python 패키지 목록
├── config/
│   └── nginx.conf         # Nginx 서버 설정 파일
├── scripts/
│   └── create_tables.sql  # MySQL DB 생성 및 테이블 스크립트
├── public/
│   └── index.html         # 기본 HTML 파일 (필요 시 CSS, JS도 포함 가능)
└── README.md              # 프로젝트 설명 문서
```

## 설정 및 실행 방법

1. **Python 패키지 설치**  
   ```bash
   cd app
   pip3 install -r requirements.txt
   ```

2. **MySQL 데이터베이스 구성**  
   ```bash
   mysql -u root -p
   source scripts/create_tables.sql;
   ```
   - 데이터베이스와 `posts` 테이블이 생성됩니다.

3. **환경 변수 설정**  
   ```bash
   export DB_HOST=localhost
   export DB_USER=root
   export DB_PASS=비밀번호
   export DB_NAME=bulletin_board
   ```
   - (또는 `.env` 파일 등에 저장하여 관리할 수 있습니다.)

4. **Flask 애플리케이션 실행 (개발용)**  
   ```bash
   cd app
   python3 flask_app.py
   ```
   - 브라우저에서 `http://localhost:8000` 접속

5. **Gunicorn + Nginx (운영용)**  
   - **Gunicorn 실행**  
     ```bash
     gunicorn --bind 127.0.0.1:8000 flask_app:app
     ```
   - **Nginx 설정**  
     - `/etc/nginx/sites-available/`에 `nginx.conf`를 복사하고 심볼릭 링크를 생성합니다.
     - 설정이 완료되면 아래 명령어로 확인 및 적용합니다.
       ```bash
       sudo nginx -t
       sudo systemctl reload nginx
       ```
     - 브라우저에서 `http://서버IP` 또는 설정한 도메인으로 접속합니다.

## 라이선스

- 원하는 라이선스를 선택하여 사용하시면 됩니다. (예: MIT License)

## 문의

- 이메일: `kye980701@gmail.com`
```
