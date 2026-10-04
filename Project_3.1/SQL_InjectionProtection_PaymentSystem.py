import sqlite3

connection = sqlite3.connect("payments.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
	id INTEGER PRIMARY KEY, 
	username TEXT UNIQUE
)
""")

cursor.execute(
	"INSERT OR IGNORE INTO customers (username) VALUES (?)",
	("diego",)
)
cursor.execute(
	"INSERT OR IGNORE INTO customers (username) VALUES (?)",
	("ale",)
)
cursor.execute(
	"INSERT OR IGNORE INTO customers (username) VALUES (?)",
	("luis",)
)

connection.commit()

username = input("Enter your username account: ")

cursor.execute(
	"SELECT id, username FROM customers WHERE username = ?",
	(username,)
)

customer = cursor.fetchone()

if customer:
    print("We found your account.")
    payment_amount = input("Enter payment amount: ")

    try:
        payment_amount = float(payment_amount)
		
        if payment_amount > 0:
            print("You have completed your payment successfully.")
        else:
            print("Invalid payment amount.")

    except ValueError:
        print("Invalid payment amount.")

else:
    print ("Customer account not found.")
    answer = input("Would you like to create an account with us?")
	
    if answer.lower() == "yes":
        print("Continue to create your account.")
    else:
        print("Payment cancelled.")

connection.close()
