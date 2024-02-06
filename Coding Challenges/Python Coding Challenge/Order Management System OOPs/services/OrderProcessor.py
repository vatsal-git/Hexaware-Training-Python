import mysql.connector

from entities.User import User
from exceptions.OrderCreationError import OrderCreationError
from exceptions.OrderNotFoundException import OrderNotFoundException
from exceptions.OrderProcessorException import OrderProcessorException
from exceptions.OrderRetrievalError import OrderRetrievalError
from exceptions.ProductCreationError import ProductCreationError
from exceptions.ProductNotFoundException import ProductNotFoundException
from exceptions.ProductRetrievalError import ProductRetrievalError
from exceptions.UnauthorizedUserError import UnauthorizedUserError
from exceptions.UserCreationError import UserCreationError
from exceptions.UserNotFoundException import UserNotFoundException
from exceptions.UserRetrievalError import UserRetrievalError
from interfaces.IOrderManagementRepository import IOrderManagementRepository


class OrderProcessor(IOrderManagementRepository):
    def __init__(self, db_context):
        self.db_context = db_context

    def createOrder(self, user, products):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor()

            # Insert user if not exists
            cursor.execute("INSERT IGNORE INTO users (user_id, username, password, role) VALUES (%s, %s, %s, %s)",
                           (user.user_id, user.username, user.password, user.role))

            # Insert order
            cursor.execute("INSERT INTO orders (user_id) VALUES (%s)", (user.user_id,))
            order_id = cursor.lastrowid  # Get the ID of the last inserted row

            # Insert products in the order
            for product in products:
                cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (%s, %s)",
                               (order_id, product.productId))

            connection.commit()
            cursor.close()
            connection.close()
            return f"Order created successfully with ID: {order_id}"

        except mysql.connector.Error as err:
            raise OrderProcessorException(f"Error creating order: {err}")

    def cancelOrder(self, userId, orderId):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor()

            # Check if the order with this user_id and order_id exist
            cursor.execute("SELECT * FROM orders WHERE user_id = %s AND order_id = %s", (userId, orderId))
            order = cursor.fetchone()

            if order:
                # Update the order status to "Canceled"
                cursor.execute("UPDATE orders SET order_status = 'Cancelled' WHERE order_id = %s", (orderId,))

                connection.commit()
                cursor.close()
                connection.close()
                return f"Order canceled successfully"
            else:
                raise OrderNotFoundException("Order not found")

        except mysql.connector.Error as err:
            raise OrderProcessorException(f"Error canceling order: {err}")

    def createProduct(self, product):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor()

            # Insert product
            cursor.execute("""
                INSERT INTO products (product_name, description, price, quantity_in_stock, type)
                VALUES (%s, %s, %s, %s, %s)
            """, (product.product_name, product.description, product.price,
                  product.quantity_in_stock, product.type))

            connection.commit()
            cursor.close()
            connection.close()
            return f"Product created successfully. Name: {product.product_name}"
        except mysql.connector.Error as err:
            raise ProductCreationError(f"Error creating product: {err}")

    def createUser(self, user):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor()

            # Insert user
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                           (user.username, user.password, user.role))
            connection.commit()

            user_id = cursor.lastrowid

            cursor.close()
            connection.close()
            return f"User created successfully with ID: {user_id}"

        except mysql.connector.Error as err:
            raise UserCreationError(f"Error creating user: {err}")

    def getAllProducts(self):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor(dictionary=True)

            # Retrieve all products
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            cursor.close()
            connection.close()
            return products

        except mysql.connector.Error as err:
            raise ProductRetrievalError(f"Error getting products: {err}")

    def getOrderByUser(self, user_id):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor(dictionary=True)

            # Retrieve orders for a user_id
            cursor.execute("""
                SELECT orders.order_id, products.product_id, products.product_name
                FROM orders
                JOIN order_products ON orders.order_id = order_products.order_id
                JOIN products ON order_products.product_id = products.product_id
                WHERE orders.user_id = %s
            """, (user_id,))
            orders = cursor.fetchall()

            cursor.close()
            connection.close()

            if not orders:
                raise OrderRetrievalError("No orders found for the user.")

            return orders

        except mysql.connector.Error as err:
            raise OrderRetrievalError(f"Error getting orders by user: {err}")

    def getUserByUsernameAndPassword(self, username, password):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return User(user['username'], user['password'], user['role']), user['user_id']
            else:
                raise UserNotFoundException("User not found with the given credentials.")

        except mysql.connector.Error as err:
            raise UserRetrievalError(f"Error retrieving user: {err}")

    def addToOrder(self, user_id, product_ids):
        try:
            connection = self.db_context.getDBConn()
            cursor = connection.cursor(dictionary=True)

            # Check if the user has an active order, if not, create one
            cursor.execute("SELECT * FROM orders WHERE user_id = %s AND order_status = 'Placed'", (user_id,))
            active_order = cursor.fetchone()

            if not active_order:
                cursor.execute("INSERT INTO orders (user_id) VALUES (%s)", (user_id,))
                connection.commit()

            # Get the order_id for the user's placed order
            cursor.execute("SELECT order_id FROM orders WHERE user_id = %s AND order_status = 'Placed'",
                           (user_id,))
            order_id = cursor.fetchone()['order_id']

            # Add the products to the order_products table
            for i, product_id in enumerate(product_ids):
                # Check if the product exists
                cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
                product = cursor.fetchone()

                if not product:
                    raise ProductNotFoundException(f"Product with ID {product_id} not found.")

                # Add the product to the order_products table
                cursor.execute("""
                    INSERT INTO order_products (order_id, product_id)
                    VALUES (%s, %s)
                """, (order_id, product_id))
                connection.commit()

            cursor.close()
            connection.close()
            return f"Products added to the order successfully."

        except mysql.connector.Error as err:
            raise OrderCreationError(f"Error adding products to order: {err}")

