import mysql.connector #including the python-sql connector library


#Taking the user and database details

while(True):
    usr=input("Username :")
    pswd=input("Password :")
    db = input("Enter Database Name :") #taking the table's database
    mydb = mysql.connector.connect( host="localhost" , username=usr , password=pswd , database=db )
    
    if mydb.is_connected():
        break
    else:
        print("Wrong Username or Password or Database!, Enter again")
        


#Taking required table details

tbl = input("Enter Table Name :")    
crsr = mydb.cursor()
crsr.execute('select * from '+tbl+';')
l = crsr.fetchall() #fetching the data from the table



#Writing the csv/xlsx file

import csv
f=open('MyFile.csv','w',newline='')
likh=csv.writer(f)
likh.writerows(l)
f.close()