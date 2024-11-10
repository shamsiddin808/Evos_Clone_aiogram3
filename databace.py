import sqlite3
from itertools import product

connect = sqlite3.connect('evos_database.db')
cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, phone INTEGER, longitude TEXT NULL, latitude TEXT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS products(img TEXT,name TEXT,price INTEGER,category TEXT)")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS savat (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER , product_name TEXT,count INTEGER)")



async def register_user(user_id , phone):
    cursor.execute("INSERT INTO users(user_id, phone) VALUES (?, ?)", (user_id, phone))
    connect.commit()


async def add_location(longitude, latitude,user_id):
    cursor.execute("UPDATE users SET longitude = ?, latitude = ? WHERE user_id = ?",
                   (longitude, latitude, user_id))
    connect.commit()

async def delete_accaunt_databace(user_id):
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id, ))
    connect.commit()



