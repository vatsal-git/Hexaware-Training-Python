from services.inventory_services import InventoryServices
from services.order_services import OrderServices
from view.menus import (
    main_menu,
    customer_management_menu,
    product_catalog_management_menu,
    order_processing_menu,
    inventory_management_menu,
    sales_reporting_menu,
    payment_processing_menu,
    product_search_recommendations_menu, error_menu
)
from services.customer_services import CustomerServices
from services.product_services import ProductServices
from utils.constants import CMD_COLOR_DEFAULT, CMD_COLOR_YELLOW, CMD_COLOR_RED
import traceback
from utils.constants import TECHSHOP_DB_DETAILS
from services.database_services import DatabaseServices


def main():
    try:
        # Database Connection
        db_services = DatabaseServices(**TECHSHOP_DB_DETAILS)
        db_services.connect()

        # Services Initialization
        customer_services = CustomerServices(db_services)
        product_services = ProductServices(db_services)
        order_services = OrderServices(db_services, customer_services, product_services)
        inventory_services = InventoryServices(db_services, product_services)

        while True:
            main_menu()
            choice = input("Enter your choice: ")

            if choice == '0':
                print("\nExiting TechShop Management System. Goodbye!")
                break

            elif choice == '1':
                customer_management_menu()
                customer_choice = input("Enter your choice: ")
                if customer_choice == '1':
                    customer_services.register_customer()
                elif customer_choice == '2':
                    customer_services.update_customer_account()
                elif customer_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '2':
                product_catalog_management_menu()
                product_choice = input("Enter your choice: ")
                if product_choice == '1':
                    product_services.add_new_product()
                elif product_choice == '2':
                    product_services.update_product_information()
                elif product_choice == '3':
                    product_services.remove_product()
                elif product_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '3':
                order_processing_menu()
                order_choice = input("Enter your choice: ")
                if order_choice == '1':
                    order_services.place_new_order()
                elif order_choice == '2':
                    order_services.track_order_status()
                elif order_choice == '3':
                    order_services.cancel_order()
                elif order_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '4':
                inventory_management_menu()
                inventory_choice = input("Enter your choice: ")
                if inventory_choice == '1':
                    inventory_services.add_product_to_inventory()
                elif inventory_choice == '2':
                    inventory_services.update_stock_quantity()
                elif inventory_choice == '3':
                    inventory_services.remove_product_from_inventory()
                elif inventory_choice == '4':
                    inventory_services.list_low_stock_products()
                elif inventory_choice == '5':
                    inventory_services.list_out_of_stock_products()
                elif inventory_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '5':
                sales_reporting_menu()
                sales_choice = input("Enter your choice: ")
                if sales_choice == '1':
                    # sales_reporting_service.generate_sales_report()
                    pass
                elif sales_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '6':
                payment_processing_menu()
                payment_choice = input("Enter your choice: ")
                if payment_choice == '1':
                    # payment_processing_service.record_payment()
                    pass
                elif payment_choice == '2':
                    # payment_processing_service.update_payment_status()
                    pass
                elif payment_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '7':
                product_search_recommendations_menu()
                product_search_choice = input("Enter your choice: ")
                if product_search_choice == '1':
                    search_str = input("Enter full/partial product name to search for: ")
                    products = product_services.get_all_products(search_str)
                    for p in products:
                        print(p)
                elif product_search_choice == '2':
                    # product_search_recommendation_service.get_product_recommendations()
                    pass
                elif product_search_choice == '0':
                    continue
                else:
                    print("Invalid choice. Please try again.")

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"{CMD_COLOR_YELLOW}\nOops! An Error Occurred.")
        print(f"{CMD_COLOR_RED}Exception Type: {type(e).__name__}")
        print(f"Exception Message: {str(e)}{CMD_COLOR_DEFAULT}")

        error_menu()
        error_choice = input("Enter your choice: ")
        if error_choice == '1':
            traceback_info = traceback.format_exc()
            print(f"\nMore Info: \n{traceback_info}")
            main()
        elif error_choice == '0':
            main()
        else:
            print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()
