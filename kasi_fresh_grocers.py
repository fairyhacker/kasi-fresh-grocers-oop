"""
=================================================================================
Kasi Fresh Grocers Console Application
=================================================================================
Student Name: Dineo Sefatsa (EDUV4953322)
Date: 21 August 2026
Description: Console based application for Kasi Fresh Grocers to manage stock and
             customer loyalty points, built using OOP principles: Classes and
             objects, inheritance, polymorphism, and exception handling with
             basic data persistence.
=================================================================================
"""

# ================================================================================
# 1.1 Classes & Objects - Customers class
# ================================================================================

class Customer: 
    def __init__(self, customer_id, name, loyalty_points=0):
        self.customer_id = customer_id
        self.name = name
        self.loyalty_points = loyalty_points

    def add_points(self, amount):
        self.loyalty_points += amount

    def redeem_points(self, amount):
        if amount > self.loyalty_points:
            raise ValueError("Not enough points to redeem.")
        self.loyalty_points -= amount

    def __str__(self):
        return f"Customer[{self.customer_id}] {self.name} - {self.loyalty_points} pts"


# ======================================================================================
# 1.2 The inventory class and provide methods to add, remove and find products by ID
# ======================================================================================

class Inventory: 
    def __init__(self):
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def find_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None  

    def total_stock_value(self):
        return sum(p.unit_price * p.quantity_in_stock for p in self.products)

# ======================================================================================
# 1.3 Create instances and print a stock list
# ======================================================================================

## I need product defined first 
class Product:
    def __init__(self, product_id, name, unit_price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock

    def restock(self, qty):
        self.quantity_in_stock += qty

    def sell(self, qty):
        if qty > self.quantity_in_stock:
            raise ValueError(f"Cannot sell {qty} of {self.name}; only {self.quantity_in_stock} in stock.")
        self.quantity_in_stock -= qty

    def display_info(self):
        return f"[{self.product_id}] {self.name} - R{self.unit_price:.2f} ({self.quantity_in_stock} in stock)"

## 1.3 build:
inventory = Inventory()

p1 = Product("P001", "Bread", 15.50, 40)
p2 = Product("P002", "Juice 1L", 35.00, 27)
p3 = Product("P003", "Pap 2kg", 20.00,35)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

print("--- Stock List ---")
for product in inventory.products:
    print(product.display_info())

# ======================================================================================
# 1.4 PerishableProduct and NonPerishableProduct 
# ======================================================================================

class PerishableProduct(Product):
    def __init__(self, product_id, name, unit_price, quantity_in_stock, expiry_date, shelf_life_days):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.expiry_date = expiry_date
        self.shelf_life_days = shelf_life_days

    def is_expired(self):
        from datetime import date
        return date.today() > self.expiry_date

class NonPerishableProduct(Product):
    def __init__(self, product_id, name, unit_price, quantity_in_stock, warranty_months):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.warranty_months = warranty_months

# ======================================================================================
# 1.5 Create a second, independent inheritance hierarchy: Employee, Cashier, Manager 
# ======================================================================================

class Employee:
    def __init__(self, employee_id, name, branch):
        self.employee_id = employee_id
        self.name = name
        self.branch = branch 

## I made calculate_pay() raise NotImplementdError on the base Employee 
    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay()")

    def display_info(self):
        return f"[{self.employee_id}] {self.name} - {self.branch}"

class Cashier(Employee):
    def __init__(self, employee_id, name, branch, hourly_rate, hours_worked):
        super().__init__(employee_id, name, branch)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, employee_id, name, branch, monthly_salary, bonus):
        super().__init__(employee_id, name, branch)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_pay(self):
        return self.monthly_salary + self.bonus
    
# ======================================================================================
# 1.6 Show inherited attributes and methods work without redefining them
# ======================================================================================

cashier1 = Cashier("E001", "Tumelo", "Johannesburg", 85.0, 160)
manager1 = Manager("E002", "Dimpho", "Johannesburg", 25000, 1800)

print(cashier1.display_info())
print(manager1.display_info())

# ======================================================================================
# 1.7 & 1.8 Polymorphism via method overriding 
# ======================================================================================

class PerishableProduct(Product):
    def __init__(self, product_id, name, unit_price, quantity_in_stock, expiry_date, shelf_life_days):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.expiry_date = expiry_date
        self.shelf_life_days = shelf_life_days

    def is_expired(self):
        from datetime import date
        return date.today() > self.expiry_date

    def display_info(self):
        base_info = super().display_info()
        status = "EXPIRED" if self.is_expired() else f"expires {self.expiry_date}"
        return f"{base_info} | Perishable, {status}"

class NonPerishableProduct(Product):
    def __init__(self, product_id, name, unit_price, quantity_in_stock, warranty_months):
        super().__init__(product_id, name, unit_price, quantity_in_stock)
        self.warranty_months = warranty_months

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | Non-perishable, {self.warranty_months}-month warranty"

# ======================================================================================
# 1.9 Demonstrate polymorphism with a mixed list
# ======================================================================================

p4 = PerishableProduct("P004", "Milk", 25.00, 30, __import__("datetime").date(2026,8, 23), 14)
p5 = NonPerishableProduct("P005", "Spoons", 135, 10, 8)

mixed_products = [p1, p2, p3, p4, p5]  

print(" --- Polymorphic display_info() ---")
for product in mixed_products:
    print(product.display_info())

mixed_employees = [cashier1, manager1]

print("\n--- Polymorphic calculate_pay() ---")
for emp in mixed_employees:
    print(f"{emp.name}: R{emp.calculate_pay():.2f}")

# ======================================================================================
# 1.10 Exception Handling - risky operations
# ======================================================================================

# Risky operation 1: selling more stock than available
try: 
    p1.sell(1200)
except ValueError as e:
    print(f"Error selling product: {e}")

# Risky operation 2: redeeming more points than a customer has 
customer1 = Customer("C001", "Boitumelo", 58)
try:
    customer1.redeem_points(450)
except ValueError as e:
    print(f"Error redeeming points: {e}")

# Risky operation 3: loading a data file that doesn't exist
try:
    with open("nonexistent_file.json", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Error loading file: {e}")

# ======================================================================================
# 1.11 Data persistence: save_to_file() & laod_from_file
# ======================================================================================

# 
import json

def save_to_file(inventory, customers, filename="kasi_data.json"):
    # Converts inventory/customer onjects into a dictionary, then writes
    # them to a JSON file so the data isn't lost when the program closes.
    # Note: only base Product fields are saved here 
    data = {
        "products": [
            {
                "type": type(p).__name__,
                "product_id": p.product_id,
                "name": p.name,
                "unit_price": p.unit_price,
                "quantity_in_stock": p.quantity_in_stock
            }
            for p in inventory.products
        ],
        "customers": [
            {
                "customer_id": c.customer_id,
                "name": c.name,
                "loyalty_points": c.loyalty_points
            }
            for c in customers
        ]
    }
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}.")
    except IOError as e:
        print(f"Error saving data: {e}")

def load_from_file(filename="kasi_data.json"):
    # Reads the JSON file back into Python dictionaries so data can be 
    # restored at the start of a new session.
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print(f"Data laoded from {filename}.")
            return data
    except FileNotFoundError:
        print(f"No saved data found ({filename}). Starting fresh.")
        return {"products": [], "customers": []}

# ======================================================================================
# 1.12 Console Menu to tie everything together
# ======================================================================================

def main():
    inventory = Inventory()
    customers = [customer1]

    # Sample starting stock so the menu has something to show 
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    while True:
        print("\n--- Kasi Fresh Grocers Menu ---")
        print("1. View stock")
        print("2. sell product")
        print("3. Manage loyalty points")
        print("4. Save & exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            for product in inventory.products:
                print(product.display_info())

        elif choice == "2":
            pid = input("Enter product ID to sell: ")
            product = inventory.find_product(pid)
            if product is None:
                print("Product not found.")
            else: 
                try:
                    qty = int(input("Enter quantity to sell: "))
                    product.sell(qty)
                    print(f"Sold {qty} of {product.name}.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "3":
            cid = input("Enter customer ID: ")
            customer = next((c for c in customers if c.customer_id == cid), None)
            if customer is None:
                print("Customer not found,")
            else:
                action = input("Add or redeem points? (a/r:) ")
                try:
                    amount = int(input("Enter amount: "))
                    if action == "a":
                        customer.add_points(amount)
                    else:
                        customer.redeem_points(amount)
                    print(f"{customer.name} now has {customer.loyalty_points} points.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "4":
            save_to_file(inventory, customers)
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

main() 


