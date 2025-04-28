import mysql.connector

# Replace these values with your actual database credentials
db_config = {
    'user': 'root',
    'password': 'Maltepe1997',
    'host': '34.143.170.115',
    'database': 'schedule_data'
}

# Establish the connection
connection = mysql.connector.connect(**db_config)

# You can now use the 'connection' object to interact with the database
