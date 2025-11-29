📘 SQL Queries — README
🧩 Introduction

SQL (Structured Query Language) is the standard language designed to manage and manipulate relational databases. SQL allows you to create, read, update, and delete data (often known as CRUD operations), as well as control access, define structures, and ensure data integrity.

This README covers the most essential SQL query types with clear explanations and examples.

📚 Table of Contents

What is SQL?

SQL Categories

Common SQL Queries

Filtering Data

Sorting and Limiting

Joining Tables

Aggregation

Subqueries

Table Management Queries

User Privileges

Indexes

Useful Notes

🔷 What is SQL?

SQL is a language used to communicate with relational database systems such as:

MySQL

PostgreSQL

SQLite

SQL Server

Oracle

It allows you to query and manage structured data stored in tables (rows × columns).

🔧 SQL Categories
1. DDL – Data Definition Language

Defines the structure of the database.

CREATE

ALTER

DROP

RENAME

TRUNCATE

2. DML – Data Manipulation Language

Modifies data inside tables.

SELECT

INSERT

UPDATE

DELETE

3. DQL – Data Query Language

Retrieves data.

SELECT

4. DCL – Data Control Language

Controls permissions.

GRANT

REVOKE

5. TCL – Transaction Control Language

Manages transaction behavior.

COMMIT

ROLLBACK

SAVEPOINT

🧩 Common SQL Queries
✔ SELECT — Retrieve data
SELECT name, age FROM students;

✔ INSERT — Add new data
INSERT INTO students (name, age) VALUES ('Nijat', 20);

✔ UPDATE — Modify existing data
UPDATE students
SET age = 21
WHERE name = 'Nijat';

✔ DELETE — Remove data
DELETE FROM students
WHERE age < 18;

🔍 Filtering Data
✔ WHERE
SELECT * FROM employees
WHERE salary > 5000;

✔ Comparison Operators

=, !=, <, >, <=, >=

✔ LIKE (pattern matching)
SELECT * FROM users
WHERE email LIKE '%gmail.com';

✔ IN
SELECT * FROM products
WHERE id IN (1, 3, 5);

✔ BETWEEN
SELECT * FROM orders
WHERE price BETWEEN 100 AND 300;

✔ IS NULL / IS NOT NULL
SELECT * FROM logs
WHERE deleted_at IS NULL;

📌 Sorting and Limiting
✔ ORDER BY
SELECT * FROM scores
ORDER BY points DESC;

✔ LIMIT
SELECT * FROM students
LIMIT 5;

✔ LIMIT with OFFSET
SELECT * FROM students
LIMIT 5 OFFSET 10;

🔗 Joining Tables
✔ INNER JOIN
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

✔ LEFT JOIN
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

✔ RIGHT JOIN
SELECT *
FROM students
RIGHT JOIN grades ON students.id = grades.student_id;

✔ FULL OUTER JOIN (PostgreSQL/SQL Server)
SELECT *
FROM table1
FULL OUTER JOIN table2 ON table1.id = table2.id;

📊 Aggregation
✔ COUNT
SELECT COUNT(*) FROM employees;

✔ SUM
SELECT SUM(price) FROM orders;

✔ AVG
SELECT AVG(score) FROM tests;

✔ GROUP BY
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

✔ HAVING (like WHERE, but for groups)
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 4000;

🌀 Subqueries
Scalar subquery
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

IN subquery
SELECT name
FROM products
WHERE id IN (SELECT product_id FROM orders);

🏗 Table Management Queries
✔ CREATE
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT
);

✔ ALTER
ALTER TABLE students ADD city VARCHAR(50);

✔ DROP TABLE
DROP TABLE students;

✔ TRUNCATE
TRUNCATE TABLE logs;

🔐 User Privileges
GRANT
GRANT SELECT, INSERT ON school.* TO 'appuser'@'localhost';

REVOKE
REVOKE INSERT ON school.* FROM 'appuser'@'localhost';

⚡ Indexes

Indexes speed up searches.

Add index
CREATE INDEX idx_email ON users(email);

Drop index
DROP INDEX idx_email ON users;

📝 Useful Notes

SQL keywords are case-insensitive (SELECT = select)

Queries should end with ;

Always back up before DROP or TRUNCATE

Use EXPLAIN in MySQL to analyze query performance

🎉 Conclusion

This README gives you a complete and clean overview of SQL queries commonly used in real applications, competitions, and Holberton projects. If you want, I can also create:

✅ A version in Azerbaijani
✅ A version with practice problems
✅ A cheat sheet (1-page summary)
✅ A more advanced README (joins, indexing, optimization)
