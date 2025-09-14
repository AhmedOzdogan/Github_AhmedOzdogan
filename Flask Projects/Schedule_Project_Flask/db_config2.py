import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12778032",
        password="GwESldtcR7",
        database="sql12778032")

Conn = get_connection()


def check_connection():
    try:
        Conn.ping(reconnect=True, attempts=3, delay=5)
        print("Connection is alive")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        Conn = get_connection()
        print("Reconnected to the database")
