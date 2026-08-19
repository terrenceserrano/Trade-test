#Library para makapag connect sa DB
import psycopg2

#Function block para sa Data Base connection
def connect_db():
    try:
        # To establish connection sa postgreSQL
        db = psycopg2.connect(
            host="localhost", #remote server address
            database="tradetest", #name of DB
            user="postgres", #username
            password="1234", #password
            port="5432" #port number
        )
        print("Connected to PostgreSQL Successfully!")
        return db

    except Exception as e:
        print("Error:", e)
        return None

#trial testing for connection
#connect_db()
