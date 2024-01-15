import sqlite3

with sqlite3.connect("SQLite.db") as db: #use connect functions to connct values.
    cursor = db.cursor() # the cursor object allows us to fetch the database.

while True:
  print("Welcome to the Ultimate Grade Control System")
  print("[V] - View Grade details")
  print("[Q] - Run a Query")
  print("[A] - Add a GRADE")
  print("[D] - Delete GRADE")
  print("[X] - EXIT")
  option = input("Enter an option from above")
  
  if option == "X":
    print("Goodbye")
    break
  if option == "V":
    cursor.execute("SELECT * FROM grade2")
    for row in cursor.fetchall():
      print(row)
  if option == "Q":
    print("Which query would you like to run?")
    print("1 - Students who are good at math")
    print("2 - Students who are good at math and english")
    print("3 - Students who are expert at math")
    print("4 - average score of english score")
    print("5 - Sum of students math score")
    print("6 - Students who need support at English")
    print("7 - Students who's effort is good")
    queryChoise = input("Enter an query option from above")

    if (queryChoise == '1'):
      Math = 5
      cursor.execute("SELECT ID FROM Grade2 WHERE Math > '{}'".format(Math))
      print("Students who are good at math")
      for row in cursor.fetchall():
        print(row)
      print("-----------------------------------------------------------")

    if (queryChoise == '2'):
      Math = 5
      English = 5
      cursor.execute("SELECT ID FROM Grade2 WHERE Math > '{}' and English > '{}' ".format(Math, English))
      print("Students who are good at math and english")
      for row in cursor.fetchall():
        print(row)
      break

      print("-----------------------------------------------------------")

    if (queryChoise == '3'):
      cursor.execute("SELECT ID, max(Math) FROM Grade2 ".format(Math))
      print("Students who are expert at math")
      for row in cursor.fetchall():
        print(row)
      break
      print("-----------------------------------------------------------")

    if (queryChoise == '4'):
      cursor.execute("SELECT avg(English) FROM Grade2 ".format(English))
      print("average score of english score")
      for row in cursor.fetchall():
        print(row)
      break
      print("-----------------------------------------------------------")

    if (queryChoise == '5'):
      cursor.execute("SELECT sum(Math) FROM Grade2 ".format(Math))
      print("Sum of students math score")
      for row in cursor.fetchall():
        print(row)
      break
      print("-----------------------------------------------------------")

    if (queryChoise == '6'):
      cursor.execute("SELECT ID, min(English) FROM Grade2 ".format(English))
      print("Students who need support at English")
      for row in cursor.fetchall():
        print(row)
      break
      print("-----------------------------------------------------------")

    if (queryChoise == '7'):
      Effort = "Good"
      cursor.execute("SELECT ID FROM Grade2 WHERE Effort = '{}'".format(Effort))
      print("Students who's effort is good")
      for row in cursor.fetchall():
        print(row)
      break  
      print("-----------------------------------------------------------")


  if option == "A":
    cursor.execute("SELECT * FROM Grade2")
    for row in cursor.fetchall():
      print(row)
      
    ID = input("Enter student ID")
    Math = input("Enter his/her Math score")
    English = input("Enter his/her Englsih score")
    Science = input("Enter his/her Science score")
    History = input("Enter his/her History score")
    Effort = input("Enter his/her Effort score")
    

    cursor.execute("INSERT INTO Grade2 (ID,Math,English,Science,History,Effort) VALUES(?,?,?,?,?,?)",(ID,Math,English,Science,History,Effort))
    db.commit(); 
    print("Grade2 now updated - added")
    cursor.execute("SELECT * FROM grade2")
    for row in cursor.fetchall():
      print(row)
    break
    print("-----------------------------------------------------------")

  if option == "D":
    
    deleteOption = input("Enter a Student ID to delete")

    cursor.execute("DELETE FROM Grade2 WHERE ID='{}'".format(deleteOption))
    db.commit();
    print("Grade2 now updated - deleted")
    cursor.execute("SELECT * FROM grade2")
    for row in cursor.fetchall():
      print(row)
    break
    print("-----------------------------------------------------------")

  else:
      break
      print("-----------------------------------------------------------")
      print("Please enter the choice that is in this list. Thank you")
      print("-----------------------------------------------------------")
