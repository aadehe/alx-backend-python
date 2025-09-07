# Python Generators with SQL Database
This project introduces the use of **Python generators** in combination with **SQL databases** to enable memory-efficient data streaming.  
The first step is to **set up a MySQL database**, seed it with data from a CSV file, and then use a generator to stream rows one by one.

---

## Learning Objectives
By completing this task, you will:
- Understand how to connect Python to a **MySQL database**.
- Create and manage **databases and tables** programmatically.
- Insert data from a **CSV file** into SQL tables.
- Implement a **generator function** to stream database rows efficiently.

---

## Requirements
- Python 3.x
- MySQL server installed locally
- `mysql-connector-python` library
- A sample dataset (`user_data.csv`)
- Git & GitHub for version control

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install mysql-connector-python
```