# Management System

A desktop application designed for managing a cosmetics business, built with **Python**, **SQLModel**, **PyQt6**, and **SQLite**.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PyQt6](https://img.shields.io/badge/PyQt-6-green?logo=pyside)
![SQLModel](https://img.shields.io/badge/SQLModel-0.0.24-purple) 
![SQLite3](https://img.shields.io/badge/SQLite-3-gray?logo=sqlite)

---

## 🚀 Features

The application includes 7 main modules:

### 🛍 Products

Manage a product inventory with the ability to create, filter, update, and delete products.

### 💳 Sales

Includes two sections:

- New Sale: Register new sales with selected products.

- Sales History: View past sales, see product details, and generate PDF invoices.

### 💄 Services

Maintain a list of offered services, including name, duration, and price. Services are displayed in cards containing all relevant information.

### 📅 Cosmetology appointments

Schedule new appointments by selecting a customer, date and time, service, and deposit. Double bookings (same date and time) are not allowed. Appointments are displayed in detailed cards by date.

### 👥 Customers

Create, update, and delete customer profiles. Generate PDF cosmetology sheets for each customer to track medical history and relevant details.

### ⌛ Treatments history

View a customer's treatment history, optionally filtering by service. Add notes or observations for each treatment session.

### 💸 Customer debt history

Track outstanding balances for customers who haven’t fully paid for their purchases. You can update existing payments or add new ones to keep accurate debt records.

---

## 🧱 Tech stack

The application was developed using **Python** as the core language.
It uses **SQLite** as the database engine, with **SQLModel** and **SQLAlchemy** for database modeling and data manipulation.
The graphical user interface (GUI) was built with **PyQt6**.
Additionally, the **ReportLab** library was used to generate PDF documents.

---

## 📬 Contact

Created by **Juani Aichino**

