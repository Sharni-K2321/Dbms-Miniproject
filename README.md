This Python script uses the mysql.connector module to connect to a MySQL
database named manufacturing_company. It defines functions to create tables
(products, customers, employees, orders) if they don't exist, and to perform
CRUD operations. The script includes functions to add new products, customers,
and employees, retrieve all records from these tables, update product stock,
delete products, and create orders with automatic stock deduction. It ensures
data integrity with foreign key constraints and handles datetime formatting
for order timestamps. The script exemplifies a structured approach to managing
a manufacturing company's database interactions in Python, offering a
foundational framework for maintaining and querying essential business data.
