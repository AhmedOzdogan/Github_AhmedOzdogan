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
    
# conn = get_connection()
# cursor = conn.cursor()

# query =  """SELECT SUM(TIMESTAMPDIFF(MINUTE, CONCAT('2000-01-01 ',starttime), CONCAT('2000-01-01 ',endtime))) AS TOTAL_MINUTES FROM teaching_schedule
# FROM teaching_schedule
# """
# cursor.execute(query)
# result = cursor.fetchone()  
# print(result[0])  # Print the total minutes

