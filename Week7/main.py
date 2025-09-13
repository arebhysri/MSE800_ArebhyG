from database import create_tables
from design_pattern import UserService, OrderService

if __name__ == "__main__":
    create_tables()
    user_service = UserService()
    order_service = OrderService()
    
    user_service.insert_user('Raju')
    order_service.insert_order('Laptop')
    
    user = user_service.get_user(0)
    order = order_service.get_order(0)
    
    print("User Details:", user)
    print("Order Details:", order) 