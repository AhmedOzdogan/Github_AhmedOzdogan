# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:03:08 2023

@author: ahmed
"""
import mysql.connector

# File path
file_path = "SQL.txt"

# Variables
variables = []

# Read lines from the file and assign to variables
with open(file_path, "r") as file:
    for line in file:
        variables.append(line.strip())


host_name = variables[0]
username = variables[1]
password = variables[2]
db_name = variables[3]

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host = host_name,
    user = username,
    password = password,
    database = db_name
)

