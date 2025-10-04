# CarRentalSystem
A streamlined, user-friendly car rental platform built with **Python**, **Streamlit**, and **SQLite**. This system allows users to browse available vehicles, make bookings, and manage rentals with real-time feedback and enterprise-grade UI polish.

---

## 📦 Features

- Browse and book available cars
- Admin dashboard for editing/deleting vehicles
- Dynamic booking validation (no overlaps, date limits)
- Inline booking buttons and rental status tracking
- Responsive UI with table overlays and background effects

---

User Management:
    a. Implement user registration and login functionality.
    b. Differentiate between customer and admin roles, each with specific privileges.
Car Management:
    c. Create a database of available cars, including their details (ID, make, model, year,
    mileage, available now, minimum rent period, maximum rent period.)
    d. Allow admins to add, update, and delete car records.
    Rental Booking:
    e. Enable customers to view available cars and their details.
    f. Implement a booking feature that allows customers to select a car, specify rental
    dates, and provide necessary details.
    g. Calculate the rental fees based on the selected car, rental duration, and any
    additional charges.
Rental Management:
    h. Allow admins to manage rental bookings, including approving or rejecting
    requests.

### Use Case
    Actors - customers
             admin
    
    Admin - Can add new car
            Can update the car
            can delete the car

            approve,cancel,reject the booking

    customers - Can book the car
                Can views all car
                Can view booked car

To run the Car Rental System locally, follow these steps to configure your environment and dependencies.
    - Python 3.8+
    - pip (Python package manager)
    - Git (optional, for cloning)
    - Streamlit (`pip install streamlit`)

--------------
#### File/Folder	Purpose
    streamlit_main.py	   --------- Main Streamlit application entry point
    models/	               --------- Contains Car, Booking, and User classes for data abstraction
    enums/	               --------- define a fixed set of named values
    user_management.py	   --------- Car management logic (add/edit/delete/list)
    booking_management.py  --------- Booking logic, validation, and status updates
    car_rental.db	       --------- SQLite database file (auto-generated)
    requirements.txt	   --------- Python dependencies for the system
    README.md	           --------- Documentation and setup guide

##### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/arebhysri/CarRentalSystem.git
cd CarRentalSystem

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run streamlit_main.py
```
--------------
###### Configuration
    The system uses SQLite as the default database (car_rental.db)
    On first run, tables are auto-created if missing


