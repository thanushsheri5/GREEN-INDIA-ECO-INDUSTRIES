import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

products = [
    ("Eco Bag", 50, "logo.png"),
    ("Green Bag", 30, "banner.jpg")
]

cursor.executemany(
    "INSERT INTO products (name, price, image) VALUES (?, ?, ?)",
    products
)

conn.commit()
conn.close()