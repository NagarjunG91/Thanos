import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='mydb')
cur = conn.cursor()
cur.execute("SELECT emp_id,emp_name FROM EMPLOYEE")

for row in cur:
    print(row)







