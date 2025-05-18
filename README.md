# coffee-store-for-jess
Welcome to Jesse's Coffee-Shop Challenge! This project is a Python-based simulation of a coffee shop with three primary models: Customer, Coffee, and Order. Each model is designed with strict attribute validation.

 Project Structure
 coffee-shop-challenge/
1. Pipfile
2. customer.py
3. coffee.py
4. order.py
5. README.md

 Models & Relationships

(a) Customer: Represents a customer with a name (1–15 characters).

Can create orders, list all their orders, and view unique coffees they have ordered.



(b) Coffee: Represents a coffee with a name (at least 3 characters).

Immutable once created.

Can list all orders and unique customers for this coffee.


(c) Order: Represents an order linked to a Customer and Coffee, with a price (1.0–10.0).

Immutable price once set.

