import pymysql


db = pymysql.connect("localhost", "root", "130e340", "company")
cursor = db.cursor()

sql = "SELECT * FROM employee WHERE address like \'%广州%\';"
cursor.execute(sql)
data = cursor.fetchall()
print(data)
for i in range(0, len(data)):
    for j in range(0, 6):
        print(str(data[i][j]), type(str(data[i][j])))