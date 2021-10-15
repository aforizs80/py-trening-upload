#
# with open("sample.txt", encoding="utf-8") as f:
#     for line in f:
#         print(line)

import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="employees",
        password="employees",
        host="localhost",
        port=3306,
        database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute(
    "create table if not exists employees (id bigint not null auto_increment, emp_name varchar(255), primary key (id))")

cur.execute("insert into employees(emp_name) values (?)", ("John Doe",))
cur.execute("insert into employees(emp_name) values (?)", ("John Doe",))
cur.execute("insert into employees(emp_name) values (?)", ("John Doe",))
conn.commit()