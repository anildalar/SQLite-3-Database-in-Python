import sqlite3

filename = input("Please enter the Database   ")

tablename = input("Please enter the table  ")

stu_name = input("Please enter student name  ")
stu_contact = input("Please enter student contact  ")

#Alway open the file
filename = filename+".sqlite3"

fo = open(filename,"a")

#1. Always Open the Db Connection
con = sqlite3.connect(filename)

cur = con.cursor()

#Create the table
cur.execute('CREATE TABLE '+tablename+' (name text, contact text)')

cur.execute("INSERT INTO "+tablename+" (name, contact) VALUES ('"+stu_name+"', '"+stu_contact+"')")

# INSERT the student data


itrableobject = cur.execute('SELECT * FROM '+tablename)
for row in itrableobject:
        print(row)

con.commit()





# Alway close DB Connection
con.close()

#Alway close the file
fo.close()