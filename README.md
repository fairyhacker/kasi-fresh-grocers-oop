# Kasi Fresh Grocers Console App (Python OOP)

A console-based inventory and customer loyalty management system for **Kasi Fresh Grocers**, built to demonstrate core object-oriented programming principles in Python: classes, inheritance, polymorphism, and exception handling.

## What it does

The app manages product stock and customer loyalty points through a simple text menu, backed by a set of OOP class hierarchies:

- **`Customer`** — tracks loyalty points, with add/redeem logic and validation
- **`Product`** — base class for inventory items, with two subclasses:
  - **`PerishableProduct`** — adds expiry date and shelf life, with expiry checking
  - **`NonPerishableProduct`** — adds warranty tracking
- **`Inventory`** — manages a collection of products (add, remove, find by ID, total stock value)
- **`Employee`** — base class for staff, with two subclasses:
  - **`Cashier`** — pay calculated from hourly rate × hours worked
  - **`Manager`** — pay calculated from monthly salary + bonus

Both `Product` and `Employee` hierarchies demonstrate **polymorphism**: calling `display_info()` or `calculate_pay()` on a mixed list of objects runs each subclass's own overridden version automatically.

**Exception handling** covers selling more stock than available, redeeming more points than a customer has, and loading a missing data file.

**Data persistence** saves inventory and customer data to a JSON file (`kasi_data.json`) and reloads it on the next run.

## Features (console menu)

1. View stock
2. Sell a product
3. Add or redeem customer loyalty points
4. Save and exit

## Tech used

- Python 3 (standard library only — no external dependencies)
- `json` module for data persistence
- `datetime` for expiry date checks

## How to run

```bash
python3 kasi_fresh_grocers.py
```

Follow the on-screen menu prompts. Data is saved to `kasi_data.json` in the same folder when you choose "Save & exit".

## Author

Dineo Sefatsa — built as part of a Higher Certificate in Data Analytics.
