import mysql.connector

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="12345",
    database="Ticket_Booking"
)


print("\n************Welcome Ticket Booking : **************")

ticketseatno=""
firstname=""
lastname=""
age=""



lst=list()
for i in range(1,51):
    lst.append(i)
fname=list()

for j in range(1,51):
    fname.append(j)
lname=list()

for k in range(1,51):
    lname.append(k)
agep=list()

for i in range(1,51):
    agep.append(i)

r=1

while r!=0:

    print("1.Book Ticket")
    print("2.Check Ticket Status")
    print("3.Cancel Ticket")
    print("4.Check Detail of Booked Ticket")
    print("5.Exit")

    choice=int(input("\nEnter your option :"))

    if choice==1:
        tic=int(input("Enter seat No :"))
        ticketseatno = tic
        if lst[tic-1]==tic:
            fname1=str(input("Enter your first Name :\n"))
            lname1=str(input("Enter your Last Name :\n"))
            age1=int(input("Enter your Age :\n"))
            firstname=fname1
            lastname=lname1
            age=age1    
            lst.pop(tic-1)
            fname.pop(tic-1)
            lname.pop(tic-1)
            agep.pop(tic-1)
            lst.insert(tic-1,'B')
            fname.insert(tic-1,fname1)
            lname.insert(tic-1,lname1)
            agep.insert(tic-1,age1)
            print("\n********************")
            print("Your Ticket is Booked")
            print("**************************\n")
        else:
            print("\n********************")
            print("Seat is Alredy Booked Try Other Seat")
            print("**************************\n")

        val = (ticketseatno,firstname,lastname,age )

        sql = "INSERT INTO ticket(ticket_seatno, first_name, last_name, a_ge) VALUES (%s, %s, %s, %s)"
        mycursor = connection.cursor()

        mycursor.execute(sql,val)
        connection.commit()



    elif choice==2:
        for k in lst:
            print(k,end="")



    elif choice==3:
        tic=int(input("Enter your seat no :"))
        if lst[tic-1]==tic:
            print("\n*********************")
            print("This Seat is Not Booked")
            print("*********************\n")
        else:
            lst.pop(tic-1)
            lst.insert(tic-1,tic)
            print("\n *********************")
            print("Your Ticket is cancelled")
            print(" *********************\n")



    elif choice==4:
        s=int(input("Enter seat no :\n"))
        s=s-1
        if fname[s]==s+1:
            print("\n *********************")
            print("\nThis seat is not booked")
            print("*********************\n")
        else:
            print("\n *********************")
            print('\nCostomerName is :',fname[s].title(),'',lname[s].title(),'and Age is :',agep[s])
            print("\n *********************")



    elif choice==5:
        r=0
        exit()

else:
    print("\n *********************")
    print("\nyou are Enter wrong keys")
    print("\n *********************")


connection.commit()