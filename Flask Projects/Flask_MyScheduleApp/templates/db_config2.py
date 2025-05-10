import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12778032",
        password="GwESldtcR7",
        database="sql12778032")

