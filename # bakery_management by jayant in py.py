# bakery_management.py

import sqlite3
import time

DB_FILE = "bakery.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Menu (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            product_price REAL NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

def seed_menu_if_empty(cursor, conn):
    cursor.execute('SELECT * FROM Menu')
    items = cursor.fetchall()
    if not items:
        sample = [
            ('Cake', 400),
            ('Bread', 50),
            ('Cookies', 100),
            ('Doughnuts', 80),
            ('Pie', 120)
        ]
        cursor.executemany('INSERT INTO Menu (product_name, product_price) VALUES (?, ?)', sample)
        conn.commit()

def show_menu(cursor):
    print("\n--- Bakery Menu ---")
    cursor.execute('SELECT * FROM Menu')
    for pid, name, price in cursor.fetchall():
        print(f"{pid}. {name} — ₹{price}")
    print()

def admin_menu(cursor, conn):
    while True:
        print("\nAdmin Menu:")
        print("1) Add Item")
        print("2) Update Item Price")
        print("3) Delete Item")
        print("4) Show Menu")
        print("5) Logout")
        ch = input("Enter choice: ").strip()
        if ch == '1':
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter price: ").strip())
                cursor.execute('INSERT INTO Menu (product_name, product_price) VALUES (?,?)', (name, price))
                conn.commit()
                print(f"Added item '{name}' priced ₹{price}")
            except:
                print("Invalid price.")
        elif ch == '2':
            show_menu(cursor)
            try:
                pid = int(input("Enter product id to update: ").strip())
                new_price = float(input("Enter new price: ").strip())
                cursor.execute('UPDATE Menu SET product_price = ? WHERE product_id = ?', (new_price, pid))
                conn.commit()
                print("Price updated.")
            except:
                print("Invalid input.")
        elif ch == '3':
            show_menu(cursor)
            try:
                pid = int(input("Enter product id to delete: ").strip())
                cursor.execute('DELETE FROM Menu WHERE product_id = ?', (pid,))
                conn.commit()
                print("Item deleted.")
            except:
                print("Invalid input.")
        elif ch == '4':
            show_menu(cursor)
        elif ch == '5':
            break
        else:
            print("Invalid choice.")
        time.sleep(1)

def customer_billing(cursor):
    cart = []
    total = 0.0
    while True:
        show_menu(cursor)
        sel = input("Enter product id to buy (or 'done' to finish): ").strip()
        if sel.lower() == 'done':
            break
        try:
            pid = int(sel)
            qty = int(input("Quantity: ").strip())
            cursor.execute('SELECT product_name, product_price FROM Menu WHERE product_id = ?', (pid,))
            row = cursor.fetchone()
            if row:
                name, price = row
                cost = price * qty
                cart.append((name, qty, price, cost))
                total += cost
                print(f"Added {qty} x {name} = ₹{cost}")
            else:
                print("Invalid product id.")
        except:
            print("Invalid input.")
    print("\n--- BILL ---")
    for name, qty, price, cost in cart:
        print(f"{name} x {qty} @ ₹{price:.2f} each = ₹{cost:.2f}")
    print(f"Total amount: ₹{total:.2f}")

def main():
    conn, cursor = init_db()
    seed_menu_if_empty(cursor, conn)
    while True:
        print("\n========================")
        print("Welcome to THE BAKERY")
        print("1) Admin Login")
        print("2) Customer Purchase")
        print("3) Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            pwd = input("Enter admin password: ").strip()
            if pwd == 'admin123':   # you can change password as per your choice
                admin_menu(cursor, conn)
            else:
                print("Wrong password!")
                time.sleep(1)
        elif choice == '2':
            customer_billing(cursor)
            input("Press Enter to continue …")
        elif choice == '3':
            print("Thank you — goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
    conn.close()

if __name__ == '__main__':
    main()
