import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', passwd='QwerAsdf@3953',
                              database="pranesh_python")


my_cursor=con.cursor()

my_cursor.execute("select * from student where college='Boston University'")

for i in my_cursor:
    print(i[0])