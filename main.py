from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	email = Column(String, unique=True, nullable=False)
	orders = relationship('Order', back_populates='user')

class Product(Base):
	__tablename__ = 'products'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	price = Column(Integer, nullable=False)
	orders = relationship('Order', back_populates='product')

class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
	quantity = Column(Integer, nullable=False)
	user = relationship('User', back_populates='orders')
	product = relationship('Product', back_populates='orders')

if __name__ == "__main__":
	engine = create_engine('sqlite:///shop.db')
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	# Retrieve all users and print their information
	print("All Users:")
	users = session.query(User).all()
	for user in users:
		print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

	# Retrieve all products and print their name and price
	print("\nAll Products:")
	products = session.query(Product).all()
	for product in products:
		print(f"Name: {product.name}, Price: {product.price}")

	# Retrieve all orders, showing the user's name, product name, and quantity
	print("\nAll Orders:")
	orders = session.query(Order).all()
	for order in orders:
		print(f"User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")

	# Update a product's price
	def update_product_price(product_id, new_price):
		product = session.query(Product).filter_by(id=product_id).first()
		if product:
			product.price = new_price
			session.commit()
			print(f"Updated Product ID {product_id} price to {new_price}")
		else:
			print(f"Product ID {product_id} not found.")

	# Delete a user by ID
	def delete_user_by_id(user_id):
		user = session.query(User).filter_by(id=user_id).first()
		if user:
			session.delete(user)
			session.commit()
			print(f"Deleted User ID {user_id}")
		else:
			print(f"User ID {user_id} not found.")
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

