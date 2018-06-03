import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='mydb')
cur = conn.cursor()
cur.execute("SELECT emp_id,emp_name FROM EMPLOYEE")
print(cur.fetchall())

#for row in cur:
#   print(row)

#with conn.cursor() as cursor:
#    sql = "INSERT INTO EMPLOYEE (emp_id, emp_name, emp_salary, emp_add) VALUES (%s, %s, %s, %s)"
#    cursor.execute(sql, (345, 'Shunya', 99999, 'nowhere'))
#
#conn.commit()


curr = conn.cursor()
curr.execute("SELECT COUNT(*) FROM EMPLOYEE")
print(curr.fetchone())




