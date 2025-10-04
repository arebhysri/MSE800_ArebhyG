from Week7.Sat.database import create_tables
from design_pattern import UserService, OrderService
from design_pattern_new import UserService as NewUserService, OrderService as NewOrderService

if __name__ == "__main__":
    create_tables()
    user_service = UserService()
    order_service = OrderService()
    
    user_service.insert_user('Raju')
    order_service.insert_order('Laptop')
    
    user = user_service.get_user(1)
    order = order_service.get_order(1)
    
    print("User Details:", user)
    print("Order Details:", order) 
    ### Using the new design pattern with singleton database connection
    new_user_service = NewUserService()
    new_order_service = NewOrderService()
    new_user_service.insert_user('Raju')
    new_order_service.insert_order('Laptop')

    new_user = new_user_service.get_user(1)
    new_order = new_order_service.get_order(1)

    print("New User Details:", new_user)
    print("New Order Details:", new_order)