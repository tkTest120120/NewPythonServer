# pip install mysql-connector-python
import sqlite3

def insert_or_Update(id , time):

    conn = sqlite3.connect("data.db")

    query = "select * from TimeDay where id = " + str(id)
    cusror = conn.execute(query)

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1

    if isRecordExist == 0:
        query = "INSERT INTO TimeDay values( null ,'" + str(time) + "')"
    else:
        query = "update TimeDay SET time = '" + str(time) + "' where id = " + str(id)

    conn.execute(query)

    query = "select * from TimeDay"
    cusror = conn.execute(query)
    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")

    conn.commit()
    conn.close()
    print("ok ok ok")

def getTime(id):

    conn = sqlite3.connect("data.db")

    query = "select * from TimeDay where id = " + str(id)
    cusror = conn.execute(query)

    day = ""

    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")
        day = row[1]

    conn.commit()
    conn.close()
    print("ok ok ok")
    return day

def insert_or_Update_Link(id , time):

    conn = sqlite3.connect("data.db")

    query = "select * from LinkAnh where id = " + str(id)
    cusror = conn.execute(query)

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1

    if isRecordExist == 0:
        query = "INSERT INTO LinkAnh values( null ,'" + str(time) + "')"
    else:
        query = "update LinkAnh SET time = '" + str(time) + "' where id = " + str(id)

    conn.execute(query)

    query = "select * from LinkAnh"
    cusror = conn.execute(query)
    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")

    conn.commit()
    conn.close()
    print("ok ok ok")

def delete_Link():

    conn = sqlite3.connect("data.db")

    query = "DELETE FROM LinkAnh"
    cusror = conn.execute(query)
    for row in cusror:
        print(f"id = {row[0]} -- time = {row[1]}")

    conn.commit()
    conn.close()
    print("Xóa dữ liệu bảng thành công")

def get_Link():

    conn = sqlite3.connect("data.db")

    query = "select * from LinkAnh"
    cusror = conn.execute(query)

    list_link = []

    for row in cusror:
        # print(f"id = {row[0]} -- time = {row[1]}")
        list_link.append(row[1])

    conn.commit()
    conn.close()
    print("ok ok ok")
    return list_link
