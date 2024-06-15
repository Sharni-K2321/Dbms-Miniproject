import mysql.connector
from datetime import datetime

# Function to connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="200517",
        database="manufacturing_company"
    )

# Function to create tables if they don't exist
def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()
   
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock INT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        position VARCHAR(255) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        customer_id INT,
        quantity INT NOT NULL,
        order_date DATETIME NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
    ''')
   
    conn.commit()
    conn.close()

# Function to add a new product
def add_product(name, price, stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)', (name, price, stock))
    conn.commit()
    conn.close()

# Function to add a new customer
def add_customer(name, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    conn.close()

# Function to add a new employee
def add_employee(name, position, salary):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)', (name, position, salary))
    conn.commit()
    conn.close()

# Function to get all products
def get_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

# Function to get all customers
def get_customers():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return customers

# Function to get all employees
def get_employees():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

# Function to update product stock
def update_product_stock(product_id, stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET stock = %s WHERE product_id = %s', (stock, product_id))
    conn.commit()
    conn.close()

# Function to delete a product
def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id = %s', (product_id,))
    conn.commit()
    conn.close()

# Function to create an order
def create_order(product_id, customer_id, quantity):
    conn = connect_to_db()
    cursor = conn.cursor()
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO orders (product_id, customer_id, quantity, order_date) VALUES (%s, %s, %s, %s)', (product_id, customer_id, quantity, order_date))
    cursor.execute('UPDATE products SET stock = stock - %s WHERE product_id = %s', (quantity, product_id))
    conn.commit()
    conn.close()

# Function to get all orders
def get_orders():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return orders

# Example usage
if __name__ == "__main__":
    # Create tables
    create_tables()

    # Add initial products
    add_product('Widget', 19.99, 100)
    add_product('Gadget', 29.99, 150)
    add_product('Thingamajig', 9.99, 200)

    # Add initial customers
    add_customer('Alice', 'alice@example.com')
    add_customer('Bob', 'bob@example.com')

    # Add initial employees
    add_employee('John Doe', 'Manager', 60000.00)
    add_employee('Jane Smith', 'Engineer', 70000.00)

    # Print all products
    products = get_products()
    print('Products:', products)

    # Print all customers
    customers = get_customers()
    print('Customers:', customers)

    # Print all employees
    employees = get_employees()
    print('Employees:', employees)

    # Create some orders
    create_order(1, 1, 10)  # Order 10 Widgets by Alice
    create_order(2, 2, 5)   # Order 5 Gadgets by Bob
    create_order(3, 1, 20)  # Order 20 Thingamajigs by Alice

    # Print all orders
    orders = get_orders()
    print('Orders:', orders)