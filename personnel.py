#Import from 2 files
from login import login, employee_login
from crud import add, read, update, delete

#Naka while loop para laging ready
while True:

    print("==============================")
    print("PERSONNEL MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Admin Login")
    print("2. Employee Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    #eto yung loop na mag add ka ng employee
    if choice == "1":

        if login(): #para ma call yung login sa login page

            while True:

                #Pag ang choices and kung mag logout
                print("========== MENU ==========")
                print("1. Add Employee") #Eto yung C sa crud
                print("2. Show List of Employees") #Eto yung R sa crud
                print("3. Update/Check Credentials") #Eto yung U sa crud
                print("4. Remove Employee") #Eto yung D sa crud
                print("5. Logout")

                #Eto naman yung pang input ng choice
                menu = input("Enter Choice: ")


                if menu == "1": #eto pag sa option 1
                    add() #add employee
                elif menu == "2": #eto pag sa option 2
                    read() #read employee details
                elif menu == "3": #eto pag sa option 3
                    update() #update employee details
                elif menu == "4": #eto pag sa option 4
                    delete() #delete employee
                elif menu == "5": #para ma break yung loop
                    break
                
                else:
                    print("==============================")
                    print("Logged Out!")
                    print("==============================")

    #eto naman yung function para sa employee login
    elif choice == "2":
        employee_login() #eto naman para matawag yung employee login function sa login page

    #for exit
    elif choice == "3":
        break

    else:
        print("Invalid Choice!")
