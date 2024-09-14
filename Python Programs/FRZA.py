#A program to convert SQL table data to an Excel file

import mysql.connector as sql #including the python-sql connector library


mydb=sql.connect(host='localhost',user='root',password='SARDEElagi',database='mydatabase')

crsr=mydb.cursor()


#using an endless 'while' loop for a continuous experience

while(True):
    crsr.execute('select CARNO from frzamt;') #demaniding the detail
    cnolst=crsr.fetchall() #stored the info in a main list to verify data redundancy
    print('1.Enter a New Car Info')
    print('2.Show all the cars available')
    print('3.Show sold cars')
    print('4.Register a Car Sold')
    print('Enter Choice or enter any invalid choice to discontinue,')
    a=input(":")
    if a=='1':
        while(True):
            cno=input("Enter Car No:")
            if (cno in cnolst) or (len(cno)!=10) : #checking the validity of the number
                print("Invalid Car No. or it is already in table, enter again") #using the number as the 'primary key'
            else:
                cnolst.append(cno) #appending it to the main list to verify redundancy
                cno="'"+cno+"'"
                break
        cbd=input("Enter Car Bodytype :");cbd="'"+cbd+"'" #adding single quotes to make it executable in sql
        while(True):
            cyr=input("Enter Car MFD Year :")
            if cyr.isdigit() and len(cyr)==4 :
                break
            else:
                print("Invalid Year, enter again")
        cmk=input('Car Make :');cmk="'"+cmk+"'" #adding single quotes to make it executable in sql
        cmdl=input('Model :');cmdl="'"+cmdl+"'" #adding single quotes to make it executable in sql
        while(True):
            cc=input('Enter Engine Size (cc) :')
            if cc.isdigit():
                break
            else:
                print('Invalid Figure, enter again')
        cpwr=input('Enter Power :')
        ctrq=input('Enter Torque :')
        cmlg=input('Enter Mileage :')
        qry='insert into frzamt values('+cno+','+cbd+','+cyr+','+cmk+','+cmdl+','+cc+','+cpwr+','+ctrq+','+cmlg+');' #final execution to insert the data
        crsr.execute(qry)
    elif a=='2': #to see all the data available in the table
        crsr.execute('select * from frzamt;')
        dta=crsr.fetchall()
        print(dta)
    elif a=='3' : #to see all the cars sold
        crsr.execute('select * from sold;')
        dta=crsr.fetchall()
        print(dta)
    elif a=='4': #to register a car as 'sold'
        while(True):
            cno=input("Enter Sold Car's No:")
            for cnoo in cnolst:
                if cno in cnoo:
                    crsr.execute('select CARNO,MAKE,MODL from frzamt;')
                    tmp=crsr.fetchall()
                    tsr=tmp[0][0]+"','"+tmp[0][1]+"','"+tmp[0][2]
                    tsr="insert into sold values('"+tsr+"');"
                    crsr.execute(tsr)
                    tstr="delete from frzamt where CARNO="+"'"+cno+"';"
                    crsr.execute(tstr)
                    break
            else:
                print('Car not found, enter again')
            break
    else:
        break
    mydb.commit()
    print('Done')
