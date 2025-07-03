# Management System

A desktop application designed for managing a cosmetics business, built with Python, SQLModel, PyQt6, and SQLite.

## System functionalities

The application includes 7 main modules:

#### 1) Products

Manage a product inventory with the ability to create, filter, update, and delete products.

#### 2) Sales

Includes two sections:

- New Sale: Register new sales with selected products.

- Sales History: View past sales, see product details, and generate PDF invoices.

#### 3) Services

Maintain a list of offered services, including name, duration, and price. Services are displayed in cards containing all relevant information.

#### 4) Cosmetology appointments

Schedule new appointments by selecting a customer, date and time, service, and deposit. Double bookings (same date and time) are not allowed. Appointments are displayed in detailed cards by date.

#### 5) Customers

Create, update, and delete customer profiles. Generate PDF cosmetology sheets for each customer to track medical history and relevant details.

#### 6) Treatments history

View a customer's treatment history, optionally filtering by service. Add notes or observations for each treatment session.

#### 7) Customer debt history

Track outstanding balances for customers who haven’t fully paid for their purchases. You can update existing payments or add new ones to keep accurate debt records.

## Technologies used

The application was developed using Python as the core language.
It uses SQLite as the database engine, with SQLModel and SQLAlchemy for database modeling and data manipulation.
The graphical user interface (GUI) was built with PyQt6 and PySide6.
Additionally, the ReportLab library was used to generate PDF documents.



## Author

Created by **Juani Aichino**

