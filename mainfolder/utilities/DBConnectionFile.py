import mysql.connector


class DBConnectionFile:
    def dbconnect(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="#2SA09me053", database="pythonmaybatch")
        # print(conn)
        mycursor = conn.cursor()
        mycursor.execute("select * from project")
        data = mycursor.fetchall()
        return data
