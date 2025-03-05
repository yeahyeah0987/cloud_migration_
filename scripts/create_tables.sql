CREATE DATABASE IF NOT EXISTS bulletin_board;
USE bulletin_board;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts (title, content, author)
VALUES
('첫 번째 게시글', '이것은 첫 번째 게시글의 내용입니다.', '관리자'),
('두 번째 게시글', '이것은 두 번째 게시글의 내용입니다.', '유저1');
