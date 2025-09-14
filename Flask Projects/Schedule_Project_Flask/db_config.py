import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Ahmed.4091",
#         database="teaching_schedule_db")
    
def get_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12778032",
        password="GwESldtcR7",
        database="sql12778032")
conn = get_connection()
query = """SELECT COALESCE(SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) / 60, 0) AS total_hour from teaching_schedule"""
cursor = conn.cursor()
cursor.execute(query)
result = cursor.fetchone()
total_hour = result[0]
print("Total hour:", total_hour)