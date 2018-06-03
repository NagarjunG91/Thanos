import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

# conn = sqlite3.connect('employee.db')

c = conn.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
             )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first , :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


emp_1 = Employee('Jane', 'Doe', 80000)
emp_2 = Employee('Mary', 'Doe', 95000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('Doe')
print(emps)

conn.close()
