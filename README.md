# Hands-On Assignment: Relational Databases with SQLAlchemy

This project demonstrates how to use SQLAlchemy to model and interact with relational databases in Python. It includes three main tables: User, Product, and Order, with relationships and CRUD operations.

# Features
- SQLAlchemy ORM models for User, Product, and Order
- Relationships: Users can have many Orders, Products can appear in many Orders
- Retrieve and display all users, products, and orders
- Update a product's price
- Delete a user by ID

# Table Structure
# User
- `id`: Integer, Primary Key
- `name`: String
- `email`: String, Unique

# Product
- `id`: Integer, Primary Key
- `name`: String
- `price`: Integer

# Order
- `id`: Integer, Primary Key
- `user_id`: Foreign Key referencing User.id
- `product_id`: Foreign Key referencing Product.id
- `quantity`: Integer

# Getting Started
1. Clone the repository:
   ```
   git clone https://github.com/JordanFleming1/-Hands-On-Assignment-Relational-Databases-with-SQLAlchemy.git
   ```
2. Install dependencies:
   ```
   pip install sqlalchemy
   ```
3. Run the main script:
   ```
   python main.py
   ```

# Usage
- The script will create a SQLite database (`shop.db`) and print all users, products, and orders.
- Functions are provided to update a product's price and delete a user by ID.


