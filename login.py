#Import file from connection.py
from connection import connect_db

#function block para sa login credentials naman
#Eto rin yung gamit ng admin for login
def login():

    #eto naman yung pag connect sa data base
    db = connect_db()

    if db is None:
        return False

    cursor = db.cursor()

    #Eto naman para manghingi ng details para maka pasok
    username = input("Username: ")
    password = input("Password: ")

    #eto yung para maka select sa query ng login table at para mag match yung username and password
    query = """
    SELECT * FROM login
    WHERE username=%s AND password=%s
    """
    #eto naman yung para mag execute ng selection
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    db.close()

    #Eto naman yung login notification
    if user:
        print("==============================")
        print("Login Successful!")
        print("==============================")
        return True
    else:
        print("==============================")
        print("Invalid Username or Password!")
        print("==============================")
        return False

#login() #eto yung function call para sa test ng page na to

#Eto naman yung fucntion para sa emplyee login gamit ang employee ID
def employee_login():

    # Connection sa database
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    employee_id = input("Enter Employee ID: ")

    #eto naman para specific lang na employee id lang ang icheck sa table
    query = """
        SELECT
            first_name,
            middle_name,
            last_name,
            department,
            position
        FROM employees
        WHERE employee_id = %s;
        """
    #Para ma select yung emplyee sa table
    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()

    if employee:
        #If tama yung login details eto yung display
        print("\n==============================")
        print("EMPLOYEE LOGIN SUCCESSFUL")
        print("==============================")

        #Eto naman yung details na lalabas
        print(f"First Name  : {employee[0]}")
        print(f"Middle Name : {employee[1]}")
        print(f"Last Name   : {employee[2]}")
        print(f"Department  : {employee[3]}")
        print(f"Position    : {employee[4]}")

     #kaya naka While loop to para lumabas yung choice na log out at bumalik sa personal management choices
        while True:

            print("\n==============================")
            print("EMPLOYEE MENU")
            print("==============================")
            print("Logout(Y/N)")

            choice = input("Enter Choice: ")

            if choice.upper() == 'Y':
                print("==============================")
                print("Logged Out!")
                print("==============================")

                #ma break yung loop pag nag enter ng yes
                break

            else:
                print("Invalid Choice!")

    else:
        #Eto naman pag mali
        print("==============================")
        print("Employee ID not found!")
        print("==============================")

    cursor.close()
    db.close()
