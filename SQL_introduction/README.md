# SQL Introduction

Welcome to the **SQL Introduction** project!

This repository provides the fundamental concepts, commands, and examples for learning **Structured Query Language (SQL)** — the standard language used to communicate with relational databases.

---

## 📌 What is SQL?

**SQL (Structured Query Language)** is used to store, manage, and manipulate data in a **relational database**.

SQL allows you to:

- Create and modify database structures  
- Insert, update, delete, and query data  
- Join tables and work with relationships  
- Manage users and permissions  

---

## 📚 Topics Covered

### 1. Basic Concepts
- What is a database?
- What is a relational database?
- Tables, rows, columns
- Primary & foreign keys
- Relationships between tables

### 2. SQL Commands

#### 🔹 DDL (Data Definition Language)
- `CREATE`
- `ALTER`
- `DROP`

#### 🔹 DML (Data Manipulation Language)
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

#### 🔹 DCL (Data Control Language)
- `GRANT`
- `REVOKE`

#### 🔹 TCL (Transaction Control Language)
- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`

---

## 🧪 Example Queries

```sql
-- Select all data
SELECT * FROM users;

-- Insert new record
INSERT INTO users (name, age) VALUES ('John', 22);

-- Update a record
UPDATE users SET age = 23 WHERE name = 'John';

-- Delete a record
DELETE FROM users WHERE name = 'John';
