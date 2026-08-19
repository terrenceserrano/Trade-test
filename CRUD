#import ng file from connection.py
from connection import connect_db

#Eto yung mga functions ng bawat option for CRUD

#function block para sa para sa C ng CRUD
def add():
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    employee_id = input("Employee ID: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    department = input("Department: ")
    position = input("Position: ")

    #Eto naman yung sa pag insert ng bagong employee sa database
    query = """
    INSERT INTO employees
    (employee_id, first_name, middle_name, last_name, birthday, department, position)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    #Eto yung argument values ng value parameter
    values = (
        employee_id,
        first_name,
        middle_name,
        last_name,
        birthday,
        department,
        position
    )

    cursor.execute(query, values)
    db.commit()

    #eto naman yung sasabihin pag success ang pag add
    print("==============================")
    print("Employee Added Successfully!")
    print("==============================")

    cursor.close()
    db.close()

#Eto naman yung function para sa R ng CRUD
def read():
    # Connection sa database
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    # Query para kunin ang lahat ng employees
    query = """
    SELECT employee_id, 
        first_name,
        middle_name,
        last_name,
        birthday,
        department,
        position
    FROM employees
    ORDER BY employee_id;
    """

    cursor.execute(query)
    employees = cursor.fetchall()

    if len(employees) == 0:
        print("\nNo employee records found.\n")
    else:
        print("\n================ EMPLOYEE LIST ================\n")

        print("{:<5} {:<15} {:<15} {:<15} {:<12} {:<20} {:<20}".format(
            "ID",
            "First Name",
            "Middle Name",
            "Last Name",
            "Birthday",
            "Department",
            "Position"
        ))

        print("-" * 110)

        for emp in employees:
            print("{:<5} {:<15} {:<15} {:<15} {:<12} {:<20} {:<20}".format(
                emp[0], #ID Number
                emp[1], #First name
                emp[2] if emp[2] else "", #Second Name
                emp[3], #Last Name
                str(emp[4]), #Birthday
                emp[5], #Department
                emp[6] #Position
            ))

    cursor.close()
    db.close()

#Eto naman yung function para sa U ng CRUD
def update():

    # Connection sa database
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    #Eto yung mag check ng employee ID na kung may babaguhin
    employee_id = input("Enter Employee ID to Update: ")

    #Cross check kung existing ang employee yung WHERE employee_id ay titingin siya duon sa employee_id column
    query = """
        SELECT
        first_name,
        middle_name,
        last_name,
        birthday,
        department,
        position
        FROM employees
        WHERE employee_id = %s;
        """
    cursor.execute(query, (employee_id,))

    #eto yung mag fetch ng data
    employee = cursor.fetchone()
    #eto naman pag walng data na nakuha
    if employee is None:
        print("==============================")
        print("Employee not found!")
        print("==============================")
        cursor.close()
        db.close()
        return

    # eto yung para sa alignment sa array
    first_name = employee[0]
    middle_name = employee[1]
    last_name = employee[2]
    birthday = employee[3]
    department = employee[4]
    position = employee[5]

    #naka while loop to kasi para gumana yung multiple update
    while True:

        #after na mnakuha yung data sa DB
        print("\n========== UPDATE EMPLOYEE ==========")
        print(f"1. First Name : {first_name}")
        print(f"2. Middle Name: {middle_name}")
        print(f"3. Last Name  : {last_name}")
        print(f"4. Birthday   : {birthday}")
        print(f"5. Department : {department}")
        print(f"6. Position   : {position}")
        print("7. Save Changes")
        print("8. Cancel")

        #eto yung para pumili ka ng papalitan mo
        choice = input("Enter Choice: ")

        #eto yung papalitan mo ng bago
        if choice == "1":
            first_name = input("Enter New First Name: ")

        elif choice == "2":
            middle_name = input("Enter New Middle Name: ")

        elif choice == "3":
            last_name = input("Enter New Last Name: ")

        elif choice == "4":
            birthday = input("Enter New Birthday (YYYY-MM-DD): ")

        elif choice == "5":
            department = input("Enter New Department: ")

        elif choice == "6":
            position = input("Enter New Position: ")

        #para ma save yung changes
        elif choice == "7":

            #eto naman para ma change and input sa DB
            query = """
            UPDATE employees
            SET first_name = %s,
                middle_name = %s,
                last_name = %s,
                birthday = %s,
                department = %s,
                position = %s
            WHERE employee_id = %s;
            """
            #yung values para mag ka laman yung %s sa DB
            values = (
                first_name,
                middle_name,
                last_name,
                birthday,
                department,
                position,
                employee_id
            )

            cursor.execute(query, values)
            db.commit()

            print("==============================")
            print("Employee Updated Successfully!")
            print("==============================")

            #para ma break yung loop after na save changes
            break

        elif choice == "8":
            print("Update Cancelled.")
            break

        else:
            print("Invalid Choice!")

    cursor.close()
    db.close()
#update() #eto yung pang call sa test ng function sa page na to

#Eto naman yung function para sa D ng CRUD
def delete():

    # Connection sa database
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    #Eto yung para mang hingi ng employee number na ma delete
    employee_id = input("Enter Employee ID: ")

    # Check kung existing ang employee atmag cross check
    query = """
    SELECT first_name, middle_name, last_name
    FROM employees
    WHERE employee_id = %s;
    """

    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()

    #eto naman pag wala yung employees sa listahan
    if employee is None:
        print("==============================")
        print("Employee not found!")
        print("==============================")
        cursor.close()
        db.close()
        return

    #Eto naman pag may data na nag match
    print("\nEmployee Found")
    print(f"Employee ID : {employee_id}")
    print(f"Name        : {employee[0]} {employee[1]} {employee[2]}") #Eto yung mag print ng query sa terminal

    #input ng sagot para i make sure na mag delete ng query
    confirm = input("\nAre you sure you want to delete this employee? (Y/N): ")

    if confirm.upper() == "Y":

        #eto yung line na mag delete sa query
        query = """
        DELETE FROM employees
        WHERE employee_id = %s;
        """

        cursor.execute(query, (employee_id,))
        db.commit()

        print("==============================")
        print("Employee Deleted Successfully!")
        print("==============================")

    #eto naman pag pinili mo mag no sa chices
    else:
        print("==============================")
        print("Delete Cancelled.")
        print("==============================")

    cursor.close()
    db.close()
#delete() function testing
