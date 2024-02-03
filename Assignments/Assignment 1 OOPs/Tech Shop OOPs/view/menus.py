from utils.constants import CMD_COLOR_YELLOW, CMD_COLOR_DEFAULT, CMD_COLOR_BLUE


def main_menu():
    print(f"{CMD_COLOR_YELLOW}\nTechShop Management System{CMD_COLOR_DEFAULT}")
    print("1. Customer Management")
    print("2. Product Catalog Management")
    print("3. Order Processing")
    print("4. Inventory Management")
    print("5. Sales Reporting")
    print("6. Payment Processing")
    print("7. Product Search and Recommendations")
    print("0. Exit")


def customer_management_menu():
    print(f"{CMD_COLOR_YELLOW}\nCustomer Management Menu{CMD_COLOR_DEFAULT}")
    print("1. Customer Registration")
    print("2. Update Customer Account")
    print("0. Back to Main Menu")


def product_catalog_management_menu():
    print(f"{CMD_COLOR_YELLOW}\nProduct Catalog Management Menu{CMD_COLOR_DEFAULT}")
    print("1. Add New Product")
    print("2. Update Product Information")
    print("3. Remove Product")
    print("0. Back to Main Menu")


def order_processing_menu():
    print(f"{CMD_COLOR_YELLOW}\nOrder Processing Menu{CMD_COLOR_DEFAULT}")
    print("1. Place New Order")
    print("2. Track Order Status")
    print("2. Cancel Order")
    print("0. Back to Main Menu")


def inventory_management_menu():
    print(f"{CMD_COLOR_YELLOW}\nInventory Management Menu{CMD_COLOR_DEFAULT}")
    print("1. Add New Product to Inventory")
    print("2. Update Stock Quantity")
    print("3. Remove Product from Inventory")
    print("4. List Low Stock Products")
    print("5. List Out of Stock Products")
    print("0. Back to Main Menu")


def sales_reporting_menu():
    print(f"{CMD_COLOR_YELLOW}\nSales Reporting Menu{CMD_COLOR_DEFAULT}")
    print("1. Generate Sales Report")
    print("0. Back to Main Menu")


def payment_processing_menu():
    print(f"{CMD_COLOR_YELLOW}\nPayment Processing Menu{CMD_COLOR_DEFAULT}")
    print("1. Record Payment")
    print("2. Update Payment Status")
    print("0. Back to Main Menu")


def product_search_recommendations_menu():
    print(f"{CMD_COLOR_YELLOW}\nProduct Search and Recommendations Menu{CMD_COLOR_DEFAULT}")
    print("1. Search for Products")
    print("2. Get Product Recommendations")
    print("0. Back to Main Menu")


def error_menu():
    print(f"{CMD_COLOR_BLUE}\nError Menu{CMD_COLOR_DEFAULT}")
    print("1. Show more details for error")
    print("0. Back to Main Menu")
