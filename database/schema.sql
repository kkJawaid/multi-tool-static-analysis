DROP DATABASE IF EXISTS multi_tool_static_analysis;
CREATE DATABASE multi_tool_static_analysis;

USE multi_tool_static_analysis;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL UNIQUE,

    CHECK (CHAR_LENGTH(user_name) >= 5),
    CHECK (CHAR_LENGTH(user_password) >= 8),
    CHECK (user_email LIKE '%@%')
);

CREATE TABLE blogs (
    blog_id INT AUTO_INCREMENT PRIMARY KEY,
    blog_title VARCHAR(255) NOT NULL,
    blog_text TEXT NOT NULL,
    published_date DATETIME NOT NULL,
    edited_date DATETIME,
    blog_status ENUM('public', 'private') NOT NULL,
    user_id INT NOT NULL,

    CHECK (CHAR_LENGTH(blog_title) >= 5),
    CHECK (CHAR_LENGTH(blog_text) >= 100),

    CONSTRAINT fk_blog_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    comment_text TEXT NOT NULL,
    published_time DATETIME NOT NULL,
    edited_time DATETIME NULL,
    user_id INT NOT NULL,
    blog_id INT NOT NULL,

    CHECK (CHAR_LENGTH(comment_text) >= 1),

    CONSTRAINT fk_comment_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_comment_blog
        FOREIGN KEY (blog_id)
        REFERENCES blogs(blog_id)
        ON DELETE CASCADE
);

CREATE TABLE bookmarks (
    bookmark_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    blog_id INT NOT NULL,
    UNIQUE (user_id, blog_id),

    CONSTRAINT fk_bookmark_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bookmark_blog
        FOREIGN KEY (blog_id)
        REFERENCES blogs(blog_id)
        ON DELETE CASCADE
);