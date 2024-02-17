import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', passwd='QwerAsdf@3953',
                              database="pranesh_python")

my_cursor = con.cursor()

my_cursor.execute("select * from student where college='NEU'")

for i in my_cursor:
    print(i[0], i[1])



"""
zip function
"""

t1=(1, 2, 3)
t2=(4, 5, 6)

for i, j in zip(t1, t2):
    print(i,j)

zipped=list(zip(t1, t2))
for i in zipped:
    print(i)