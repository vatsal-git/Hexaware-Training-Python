import os
from dotenv import load_dotenv
load_dotenv()

# REGEX Constants
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
PHONE_REGEX = r'^\d{10}$'

# ENUM Constants
ORDER_STATUS_ENUM = ['Pending', 'Shipped', 'Delivered', 'Cancelled']

# Terminal Color Codes
CMD_COLOR_DEFAULT = "\033[0m"
CMD_COLOR_YELLOW = "\033[93m"
CMD_COLOR_RED = "\033[91m"
CMD_COLOR_BLUE = "\033[94m"

# DB Details
TECHSHOP_DB_DETAILS = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database_name': "techshop"
}
