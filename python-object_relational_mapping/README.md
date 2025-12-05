# Python - Object Relational Mapping

This project explores how to connect Python programs to MySQL databases using two different techniques:

1. **Direct SQL queries** using the `MySQLdb` module  
2. **Object Relational Mapping (ORM)** using `SQLAlchemy`

The goal is to understand how data can be accessed both by writing SQL manually and by using Python classes that automatically interact with the database.

---

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Explain what **Object Relational Mapping (ORM)** is  
- Connect to a MySQL database using Python  
- Run SQL queries in Python with `MySQLdb`  
- Create Python classes mapped to MySQL tables using `SQLAlchemy`  
- Use CRUD operations (Create, Read, Update, Delete) with ORM  
- Understand relationships (one-to-many, many-to-one) between tables  
- Use `session` objects to interact with the database using ORM  

---

## 🛠 Requirements

- Allowed editors: `vi`, `vim`, `emacs`  
- Python scripts must be compatible with **Python 3.8+**  
- Tested on Ubuntu 20.04 LTS  
- MySQL version: **MySQL 8.0+**  
- SQLAlchemy version: **1.4.x**  
- Code must follow **PEP8 style**  
- All files must be executable  
- All modules must have documentation  

---

## 📦 Installing Required Packages

### Install MySQL server
```bash
sudo apt-get install mysql-server
