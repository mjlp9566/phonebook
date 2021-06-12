import sqlite3 as sq
import sys
connection=sq.connect('phonebook.db')
cursor=connection.cursor()
#cursor.execute('''CREATE TABLE phoneinfo(Mobile_Number,Name1,Name2);''')
def Input():
 global command,user_split
 print("---------------------------------------------------------------------")
 print("COMMANDS:whois phone-number,add phone-number info,search keyword,quit")
 print("----------------------------------------------------------------------\n")
 user_split=input("Enter the command:").split()
 command=user_split[0] 
def add():
 number=user_split[1]
 name1=user_split[2]
 name2=user_split[3]
 result=cursor.execute("""INSERT INTO phoneinfo(Mobile_Number,Name1,Name2)
 VALUES(?,?,?);""",(number,name1,name2))

def view():
 result=cursor.execute("SELECT * FROM phoneinfo")
 for i in result:
     print(i[0],":",i[1],i[2])

def who_is():
 number=user_split[1]
 result=cursor.execute("""SELECT * FROM phoneinfo
 WHERE Mobile_Number=?""",(number,)) 
 for i in result:
     print(i[0],":",i[1],i[2])

def search():
 name=user_split[1]
 result_1=cursor.execute("""SELECT * FROM phoneinfo
 WHERE Name1=?""",(name,))
 for i in result_1:
     print(i[0],":",i[1],i[2])
 
def search2():
 name=user_split[1]
 result_2=cursor.execute("""SELECT * FROM phoneinfo
 WHERE Name2=?""",(name,))
 for i in result_2:
     print(i[0],":",i[1],i[2])

def delete():
        name=user_split[1]
        cursor.execute("""DELETE FROM phoneinfo
        WHERE Name1=?""",(name,))
        connection.commit()

while True:
 Input()
 if command=='add':
  add()
  connection.commit()
 elif command=='view':
  view()
 elif command=="whois":
  who_is()
 elif command=="quit":
  sys.exit()
 elif command=="search":
  search()
  search2()
 elif command=="delete":
      delete()
 else:
  pass
