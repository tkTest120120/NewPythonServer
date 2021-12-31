# pip install mysql-connector-python
import mysql.connector

def insert_or_Update_Time(id , time):
    mydb = mysql.connector.connect(
        host="37.59.55.185",
        user="JnWiETIzRg",
        password="47tKHpVqR3",
        database="JnWiETIzRg"
    )

    mycursor = mydb.cursor()

    query = "select * from TimeDay where id = " + str(id)
    mycursor.execute(query)
    cusror = mycursor.fetchall()

    isRecordExist = 0

    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")
        isRecordExist = 1

    if isRecordExist == 0:
        query = "INSERT INTO TimeDay values( null ,'" + str(time) + "')"
    else:
        query = "update TimeDay SET time = '" + str(time) + "' where id = " + str(id)

    mycursor.execute(query)

    # query = "select * from TimeDay"
    # cusror = mycursor.fetchall()
    # for row in cusror:
    #     print(f"id = {row[0]} -- time = {row[1]}")

    mydb.commit()
    mydb.close()
    print("ok ok ok")

def getTime(id):
    mydb = mysql.connector.connect(
        host="37.59.55.185",
        user="JnWiETIzRg",
        password="47tKHpVqR3",
        database="JnWiETIzRg"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM TimeDay where id = " + str(id))

    myresult = mycursor.fetchall()

    day = ""

    for row in myresult:
        print(f"id = {row[0]} -- time = {row[1]}")
        day = row[1]

    mydb.commit()
    mydb.close()
    print("ok ok ok")
    return day

def insert_or_Update_Link(id , link):
    mydb = mysql.connector.connect(
        host="37.59.55.185",
        user="JnWiETIzRg",
        password="47tKHpVqR3",
        database="JnWiETIzRg"
    )

    mycursor = mydb.cursor()

    query = "select * from LinkAnh where id = " + str(id)
    mycursor.execute(query)
    cusror = mycursor.fetchall()

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1
        print(f"id = {row[0]} -- time = {row[1]}")

    if isRecordExist == 0:
        query = "INSERT INTO LinkAnh values( null ,'" + str(link) + "')"
    else:
        query = "update LinkAnh SET link = '" + str(link) + "' where id = " + str(id)

    mycursor.execute(query)

    # query = "select * from LinkAnh"
    # cusror = conn.execute(query)
    # for row in cusror:
    #     print(f"id = {row[0]} -- time = {row[1]}")

    mydb.commit()
    mydb.close()
    print("ok ok ok")

def delete_Link():

    mydb = mysql.connector.connect(
        host="37.59.55.185",
        user="JnWiETIzRg",
        password="47tKHpVqR3",
        database="JnWiETIzRg"
    )

    mycursor = mydb.cursor()

    query = "DELETE FROM LinkAnh"
    mycursor.execute(query)
    cusror = mycursor.fetchall()
    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")

    mydb.commit()
    mydb.close()
    print("Xóa dữ liệu bảng thành công")

def get_Link():
    mydb = mysql.connector.connect(
        host="37.59.55.185",
        user="JnWiETIzRg",
        password="47tKHpVqR3",
        database="JnWiETIzRg"
    )

    mycursor = mydb.cursor()

    query = "select * from LinkAnh"
    mycursor.execute(query)
    cusror = mycursor.fetchall()

    list_link = []

    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")
        list_link.append(row[1])

    mydb.commit()
    mydb.close()
    print("ok ok ok")
    return list_link