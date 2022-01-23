import sqlite3

# create database and tables
database = sqlite3.connect('database.db')
cursor = database.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)
"""
cursor.execute("INSERT INTO users (name,password) VALUES ('prabal','pathak')")
database.commit()
"""
database.close()
print("completed")
