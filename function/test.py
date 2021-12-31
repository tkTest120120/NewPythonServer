import mysql.connector

mydb = mysql.connector.connect(
    host="37.59.55.185",
    user="JnWiETIzRg",
    password="47tKHpVqR3",
    database="JnWiETIzRg"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM TimeDay")

myresult = mycursor.fetchall()

day = ""

for row in myresult:
  print(f"id = {row[0]} -- time = {row[1]}")
  day = row[1]

  mydb.commit()
  mydb.close()