USE multi_tool_static_analysis;

INSERT INTO users (user_name, user_password, user_email)
VALUES
('alice01', 'Password1!', 'alice@example.com'),
('bobsmith', 'Password1!', 'bob@example.com'),
('charlie7', 'Password1!', 'charlie@example.com'),
('david99', 'Password1!', 'david@example.com'),
('evejones', 'Password1!', 'eve@example.com');

INSERT INTO blogs
(blog_title, blog_text, published_date, edited_date, blog_status, user_id)
VALUES
(
'Getting Started with Python',
'Python is a versatile programming language used in web development, automation, machine learning, scientific computing, scripting, backend development, and cybersecurity. This article introduces the basic syntax, variables, functions, and control structures needed to begin learning Python effectively.',
NOW(),
NULL,
'public',
1
),

(
'Understanding SQL',
'Structured Query Language is the standard language for relational databases. It allows developers to create tables, retrieve data, modify records, enforce constraints, and manage transactions. Mastering SQL is essential for backend development and database security.',
NOW(),
NULL,
'public',
2
),

(
'Introduction to FastAPI',
'FastAPI is a modern Python framework for building APIs quickly using type hints and automatic validation. It includes automatic OpenAPI documentation, dependency injection, asynchronous support, and excellent performance compared with many traditional frameworks.',
NOW(),
NULL,
'public',
3
),

(
'Private Draft',
'This draft contains notes about future improvements, architectural decisions, experimental plans, and implementation details that are not yet ready for publication. The article remains private until the author completes revisions and testing.',
NOW(),
NULL,
'private',
1
);

INSERT INTO comments
(comment_text, published_time, edited_time, user_id, blog_id)
VALUES
(
'Great introduction. I learned several new concepts from this article.',
NOW(),
NULL,
2,
1
),

(
'Could you include examples using prepared statements in a future article?',
NOW(),
NULL,
3,
2
),

(
'Very clear explanation of FastAPI. Looking forward to the authentication section.',
NOW(),
NULL,
4,
3
);

INSERT INTO bookmarks
(user_id, blog_id)
VALUES
(2,1),
(3,1),
(3,2),
(4,3),
(5,1);