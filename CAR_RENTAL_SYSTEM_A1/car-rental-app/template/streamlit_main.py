import streamlit as st
# filepath: c:\Users\Administrator\Documents\GitHub\MSE800_ArebhyG\CAR_RENTAL_SYSTEM_A1\CarRentalSystem\Template\streamlit_main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Factory.users_factory import UserFactory
from Factory.car_factory import CarFactory
from Factory.booking_factory import BookingFactory

from Enum.usre_role import user_role
from Enum.bookingAction import BookingAction
# from Enum.bookingAction import BookingAction as booking_action
from Enum.carType import CarType
from Enum.fuelType import FuelType
from datetime import datetime, timedelta

from Models.user import User
from Models.car import Car
from Models.booking import Booking
import pandas as pd
from PIL import Image
import requests
from PIL import Image
from io import BytesIO

# Booking section
from datetime import datetime, timedelta


# Initialize services using Singleton factories
user_mgmt = UserFactory.get_instance()
car_mgmt = CarFactory.get_instance()
booking_mgmt = BookingFactory.get_instance()

st.set_page_config(page_title="Car Rental Dashboard", layout="wide")

st.markdown("""
        <style>
        .table-header div {
            font-weight: 600;
            font-size: 15px;
            padding-bottom: 4px;
        }
        .table-row div {
            font-size: 14px;
            padding-top: 2px;
            padding-bottom: 2px;
        }
        div[data-testid="stSelectbox"] {
            margin-top: -6px;
            margin-bottom: -6px;
        }
        .st-emotion-cache-1ui2hlr {
            margin-bottom: 0rem;
            min-height: 0rem;
        }
        button[kind="primary"] {
            margin-top: -2px;
        }
        .marquee {
            width: 100%;
            overflow: hidden;
            white-space: nowrap;
            box-sizing: border-box;
            animation: marquee 50s ease-out infinite;
            font-size: 21px;
            color: #23037c;
            padding: 6px 0;
            font-weight: bold;
        }

        @keyframes marquee {
            0%   { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        </style>

        <div class="marquee">
            🚗 Welcome to Car Rental System — Manage bookings, update statuses, and explore our fleet in real time!
        </div>
        </style>
    """, unsafe_allow_html=True)


# Session state for login
if "user" not in st.session_state:
    st.session_state.user = None

# Session state keys
SESSION_USER_KEY = 'user'
SESSION_ROLE_KEY = 'role'
SESSION_LOGIN_TIME_KEY = 'login_time'
SESSION_TIMEOUT_MINUTES = 30
SESSION_USER_NAME = 'name'

# Function to check session timeout
def is_session_active() -> bool:
    if SESSION_LOGIN_TIME_KEY in st.session_state:
        login_time = st.session_state[SESSION_LOGIN_TIME_KEY]
        if datetime.now() - login_time < timedelta(minutes=SESSION_TIMEOUT_MINUTES):
            return True
    return False

# Function to reset session
def reset_session():
    for key in [SESSION_USER_KEY, SESSION_ROLE_KEY, SESSION_LOGIN_TIME_KEY]:
        if key in st.session_state:
            del st.session_state[key]


# Login section
def login_ui():
    st.sidebar.title("Login")
    email = st.sidebar.text_input("Email",key="login_email")
    password = st.sidebar.text_input("Password", type="password",key="login_password")
    if st.sidebar.button("Login",key="login_button"):
        user_data = user_mgmt.authenticate_user(email, password)
        if user_data:
            if 'password' not in user_data:
                user_data['password'] = ''  # or None
            if 'created_at' not in user_data:
                user_data['created_at'] = ''
            st.session_state[SESSION_USER_NAME] = user_data['name']
            st.session_state[SESSION_USER_KEY] = User(**user_data)
            st.session_state[SESSION_ROLE_KEY] = user_data['role']
            st.session_state[SESSION_LOGIN_TIME_KEY] = datetime.now()
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

# Registration section
def registration_ui():
    st.sidebar.title("Register")
    name = st.sidebar.text_input("Name", key="register_name")
    email = st.sidebar.text_input("Email", key="register_email")
    password = st.sidebar.text_input("Password", type="password", key="register_password")
    role = st.sidebar.selectbox("Role", [user_role.ADMIN, user_role.CUSTOMER], key="register_role")
    if st.sidebar.button("Register", key="register_button"):
        user_id = user_mgmt.register_user(name, role, email, password)
        if user_id:
            st.success("Registration successful!")
        else:
            st.error("Registration failed.")

# Function to display add car form
def display_add_car_form():
    st.title("Add New Car")
    manufacturer = st.text_input("Manufacturer")
    model = st.text_input("Model")
    year = st.text_input("Year")
    mileage = st.number_input("Mileage", min_value=0)
    is_Available = st.checkbox("Is Available", value=True)
    min_rental_period = st.number_input("Minimum Rental Period (days)", min_value=1)
    max_rental_period = st.number_input("Maximum Rental Period (days)", min_value=1)
    car_rate = st.number_input("Car Rate ($/day)", min_value=0.0, format="%.2f")
    car_type = st.selectbox("Car Type", [CarType.CONVERTIBLE,CarType.COUPE,CarType.HATCHBACK,CarType.SEDAN,CarType.SUV,CarType.TRUCK,CarType.VAN],key="car_type")
    fuel_type = st.selectbox("Fuel Type", [FuelType.PETROL,FuelType.DIESEL,FuelType.ELECTRIC,FuelType.HYBRID],key="fuel_type")
    registration_number = st.text_input("Registration_number")

    if st.button("Add Car"):
        car_creater = CarFactory.get_instance()
        car_id = car_mgmt.add_car(manufacturer, model, year, mileage, is_Available, min_rental_period, max_rental_period, car_rate,registration_number,car_type,fuel_type)
        if car_id:
            st.success(f"Car added successfully with ID {car_id}.")
            st.session_state['show_add_car'] = False
            st.rerun()
        else:
            st.error("Failed to add car. Please check the details and try again.")
    if st.button("Back to Dashboard"):
        st.session_state['show_add_car'] = False
        st.rerun()

# Function to display edit car form
def display_edit_car_form(car_id: int):
    car_data = car_mgmt.get_car_by_id(car_id)
    if not car_data:
        st.error("Car not found.")
        st.session_state['show_edit_car'] = False
        st.rerun()

    car = Car(**car_data)
    st.title(f"Edit Car ID {car.car_id}")

    manufacturer = st.text_input("Manufacturer", value=car._manufacturer)
    model = st.text_input("Model", value=car._model)
    year = st.text_input("Year", value=car.year)
    mileage = st.number_input("Mileage", min_value=0, value=car.get_mileage())
    is_available = st.checkbox("Is Available", value=car.is_available)
    min_rental_period = st.number_input("Minimum Rental Period (days)", min_value=1, value=car._min_rental_period)
    max_rental_period = st.number_input("Maximum Rental Period (days)", min_value=1, value=car._max_rental_period)
    car_rate = st.number_input("Car Rate ($/day)", min_value=0.0, format="%.2f", value=car.get_rate())

    # Car Type dropdown with index
    car_type_options = [
        CarType.CONVERTIBLE,
        CarType.COUPE,
        CarType.HATCHBACK,
        CarType.SEDAN,
        CarType.SUV,
        CarType.TRUCK,
        CarType.VAN
    ]
    car_type_index = car_type_options.index(car.get_car_type()) if car.get_car_type() in car_type_options else 0
    car_type = st.selectbox("Car Type", car_type_options, index=car_type_index)

    # Fuel Type dropdown with index
    fuel_type_options = [
        FuelType.PETROL,
        FuelType.DIESEL,
        FuelType.ELECTRIC,
        FuelType.HYBRID
    ]
    fuel_type_index = fuel_type_options.index(car.get_fuel_type()) if car.get_fuel_type() in fuel_type_options else 0
    fuel_type = st.selectbox("Fuel Type", fuel_type_options, index=fuel_type_index)

    registration_number = st.text_input("Registration Number", value=car.get_registration_number())

    if st.button("Update Car", key="update_car_btn"):
        if car_mgmt.update_car(
            car.car_id, manufacturer, model, year, mileage,
            is_available, min_rental_period, max_rental_period,
            car_rate, car_type, fuel_type, registration_number
        ):
            st.success(f"Car ID {car.car_id} updated successfully.")
            st.session_state['show_edit_car'] = False
            del st.session_state['edit_car_id']
            st.rerun()
        else:
            st.error("Failed to update car. Please check the details and try again.")

    if st.button("Back to Dashboard", key="back_to_dashboard_btn"):
        st.session_state['show_edit_car'] = False
        del st.session_state['edit_car_id']
        st.rerun()

# Function to display customer dashboard
def display_customer_dashboard():
    st.title("Customer Dashboard")
    
    st.write(f"Welcome, {st.session_state[SESSION_USER_KEY].name}!")
    if st.button("Logout"):
        logout_user()
    #table display
    cars = car_mgmt.list_cars()

    if cars:
        st.subheader("Available Cars")

        # Table header
        header_cols = st.columns([2, 3, 2, 2, 2, 2])
        headers = ["Registration #", "Manuefacture & Model", "Year", "Mileage", "Rate ($/day)", "Action"]
        for col, label in zip(header_cols, headers):
            col.markdown(f"**{label}**")

        # Table rows
        for car_data in cars:
            car_data['is_available'] = car_data.get('is_available', False)
            car = Car(**car_data)

            if car.is_available:
                row = st.columns([2, 3, 2, 2, 2, 2])
                row[0].write(car.get_registration_number())
                row[1].write(f"{car._manufacturer} {car._model}")
                row[2].write(car.year)
                row[3].write(car.get_mileage())
                row[4].write(f"${car.get_rate():.2f}")

                with row[5]:
                    if st.button("Book", key=f"book_{car.car_id}" , help="Book your Car"):
                        st.session_state['book_car_id'] = car.car_id
                        st.session_state['show_book_car'] = True
                        st.rerun()
    else:
        st.info("No cars available for booking.")

    st.subheader("My Bookings")
    # Fetch all bookings
    bookings = booking_mgmt.get_all_bookings()

    # Filter bookings for the logged-in user
    user_bookings = [b for b in bookings if b['user_id'] == st.session_state[SESSION_USER_KEY].user_id]

    if user_bookings:
        
        # Prepare data for table
        booking_rows = []
        for booking_data in user_bookings:
            booking = Booking(**booking_data)
            booking_rows.append({
                "Booking ID": booking.registration_number,
                "Car Model": booking.model,
                "Status": booking._rental_status,
                "Start Date": booking.start_date,
                "End Date": booking.end_date,
                "Price": booking.get_price()
            })

        # Display table
        df = pd.DataFrame(booking_rows)
        st.dataframe(df, use_container_width=True)

    else:
        st.info("You have no bookings.")


# Car listing section
def car_listing_ui():
    st.header("Available Cars")
    cars = car_mgmt.get_all_cars()
    if cars:
         # Table header
        header_cols = st.columns([1, 2, 3, 2, 2, 3, 2])
        header_labels = ["ID", "Manufacturer", "Model (Year)","Milage (Fuel Type)", "Available", "Rate", "Actions"]
        for col, label in zip(header_cols, header_labels):
            col.markdown(f"**{label}**")

        # Table rows
        for car_data in cars:
            if 'is_Available' in car_data:
                car_data['is_available'] = car_data.pop('is_Available')
            car = Car(**car_data)

            row = st.columns([1, 2, 3, 2, 2, 3, 2])
            row[0].write(car.get_registration_number())
            row[1].write(car._manufacturer)
            row[2].write(f"{car._model} ({car.year}) ({car.get_car_type()})")
            row[3].write(f"{car.get_mileage()} ({car.get_fuel_type()})")
            row[4].write("Yes" if car.is_available else "No")
            row[5].write(f"${car.get_rate()}/day")

            # Inline buttons
            with row[6]:
                col_edit, col_delete = st.columns([1, 1])
                if col_edit.button("✏️", key=f"edit_{car.car_id}", help="Edit"):
                    st.session_state['edit_car_id'] = car.car_id
                    st.session_state['show_edit_car'] = True
                    st.rerun()

                if col_delete.button("🗑️", key=f"delete_{car.car_id}", help="Delete"):
                    if car_mgmt.delete_car(car.car_id):
                        st.success(f"Car {car.car_id} deleted successfully.")
                    else:
                        st.error(f"Failed to delete Car {car.car_id}.")
                    st.rerun()
    else:
        st.info("No cars available. Please add new cars.")
    

def booking_ui(car_id: int):
    car_data = car_mgmt.get_car_by_id(car_id)
    if not car_data:
        st.error("Car not found.")
        st.session_state['show_book_car'] = False
        st.rerun()

    # Normalize key casing
    car_data['is_available'] = car_data.pop('is_Available', car_data.get('is_available', False))

    car = Car(**car_data)
    st.title(f"Book Car ID {car.car_id} - {car._manufacturer} {car._model}")
    st.write(f"You can book this car for up to **{car_data['max_rental_period']} days**, if available.")

    # Fetch booked dates
    booked_dates = booking_mgmt.get_booked_dates(car.car_id)
    booked_set = set(booked_dates)

    today = datetime.today().date()
    max_date = today + timedelta(days=90)

    # Generate available dates
    available_dates = [
        today + timedelta(days=i)
        for i in range((max_date - today).days + 1)
        if (today + timedelta(days=i)) not in booked_set
    ]

    if not available_dates:
        st.warning("No available dates for this car in the next 90 days.")
        return

    # Select start and end dates
    start_date = st.selectbox("Start Date", available_dates)
    end_options = [
        d for d in available_dates
        if d > start_date and (d - start_date).days <= car_data['max_rental_period']
    ]

    if not end_options:
        st.warning("No valid end dates available for the selected start date.")
        return

    end_date = st.selectbox("End Date", end_options)

    # Booking logic
    if st.button("Book Now", key="book_now_btn"):
        selected_range = {
            start_date + timedelta(days=i)
            for i in range((end_date - start_date).days + 1)
        }

        if start_date >= end_date:
            st.error("End date must be after start date.")
        elif selected_range & booked_set:
            st.error("Selected range overlaps with existing bookings.")
        elif (end_date - start_date).days > car_data['max_rental_period']:
            st.error(f"Booking period exceeds maximum of {car_data['max_rental_period']} days.")
        elif SESSION_USER_KEY not in st.session_state or not hasattr(st.session_state[SESSION_USER_KEY], 'user_id'):
            st.error("User not logged in. Please log in to book a car.")
        else:
            booking_id = booking_mgmt.create_booking(
                car_id=car_id,
                user_id=st.session_state[SESSION_USER_KEY].user_id,
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat(),
                car_rate=car.get_rate()
            )
            if booking_id:
                st.success(f"Booking created successfully! ID: {booking_id}, Awaiting approval by Admin")
                st.session_state['show_book_car'] = False
                del st.session_state['book_car_id']
                st.rerun()
            else:
                st.error("Booking failed.")

    if st.button("🔙", key="back_dashboard_booking"):
        st.session_state['show_book_car'] = False
        del st.session_state['book_car_id']
        st.rerun()


# Function to handle user logout
def logout_user():
    reset_session()
    st.success("Logged out successfully.")
    st.rerun()

# Admin panel
def admin_ui():
    st.header("Admin Panel")
    col1, col2 = st.columns([4, 1])  # Adjust ratio as needed

    with col1:
        st.write(f"Welcome, {st.session_state[SESSION_USER_KEY].name}!")

    with col2:
        if st.button("Logout"):
            logout_user()
    if st.button("Add New Car"):
        st.session_state['show_add_car'] = True
        st.rerun()
    car_listing_ui()

    st.subheader("All Bookings")
    bookings = booking_mgmt.get_all_bookings()
    #table display
    if bookings:

        #table header
        header_cols = st.columns([1, 1, 1, 1, 2, 2])
        headers = ["Id", "User Name", "Model","Rental Status","Update booking Status"]
        for col, label in zip(header_cols,headers):
            col.markdown(f"**{label}**")
            
        #table rows
        for booking in bookings:
            row=st.columns([1, 1, 1, 1, 2,2])
            row[0].write(f"<div class='table-row'>{booking['registration_number']}</div>", unsafe_allow_html=True)
            row[1].write(f"<div class='table-row'>{booking['name']}</div>", unsafe_allow_html=True)
            row[2].write(f"<div class='table-row'>{booking['model']}</div>", unsafe_allow_html=True)
            row[3].write(f"<div class='table-row'>{booking['rental_status']}</div>", unsafe_allow_html=True)
            
            status_options = [action.value for action in BookingAction]
            current_status = booking['rental_status']
            index = status_options.index(current_status) if current_status in status_options else 0

            new_status = row[4].selectbox(
                label="",
                options=status_options,
                index=index,
                key=f"status_select_{booking['booking_id']}"
            )

            if row[5].button("Update", key=f"update_btn_{booking['booking_id']}"):
                success = booking_mgmt.update_booking_status(booking['booking_id'], new_status)
                if success:
                    st.success(f"Booking {booking['booking_id']} updated to {new_status}.")
                    st.rerun()
                else:
                    st.error("Failed to update status.")

# Main app logic
def main():
    st.image(
        "https://static.vecteezy.com/system/resources/previews/008/652/609/non_2x/car-rental-social-header-cover-template-flat-cartoon-background-illustration-vector.jpg",
        use_container_width=True
    )
    if SESSION_USER_KEY not in st.session_state or not is_session_active():
        login_ui()
        registration_ui()
    else:
        # Default user avatar
        st.sidebar.image(
            "https://cdn-icons-png.flaticon.com/512/149/149071.png",
            width=100,
        )
        st.sidebar.write(f"Logged in as: {st.session_state[SESSION_USER_NAME]} ({st.session_state[SESSION_ROLE_KEY]})")
        if st.session_state[SESSION_ROLE_KEY] == user_role.ADMIN:
            if 'show_add_car' in st.session_state and st.session_state['show_add_car']:
                display_add_car_form()
            elif st.session_state.get('show_edit_car') and st.session_state.get('edit_car_id') is not None:
                display_edit_car_form(st.session_state['edit_car_id'])
            else:
                admin_ui()
        elif st.session_state[SESSION_ROLE_KEY] == user_role.CUSTOMER:
            if 'show_book_car' in st.session_state and st.session_state['show_book_car'] and 'book_car_id' in st.session_state:
                booking_ui(st.session_state['book_car_id'])
            else:
                display_customer_dashboard()
        else:
            st.error("Invalid user role. Please contact support.")
            reset_session()
            st.rerun()

if __name__ == "__main__":
    main()
