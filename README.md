# python-modules
# Fee Management System

## Overview
The **Fee Management System** is a Python-based application that automates fee payment notifications via email. The system helps administrators manage student fee statuses by sending reminders to students with pending fees and confirmation messages to those who have completed their payments.

## Features
- **Admin Authentication**: Secure login with OTP verification.
- **Student Fee Status Management**: Allows the admin to update fee statuses.
- **Automated Email Notifications**:
  - Sends reminders to students with pending fees.
  - Sends confirmation emails to students with cleared fees.
- **User-friendly Menu**: Provides options for editing student data and sending emails.

## Tech Stack
- **Python**: Core programming language.
- **smtplib**: Used for sending emails via SMTP.
- **random**: Used for OTP generation.

## Files and Functionalities
- **`main.py`**: The main script that handles admin login, user data, and menu-driven operations.
- **`otp.py`**: Generates and sends OTP for admin authentication.
- **`feepending.py`**: Sends reminder emails to students with pending fees.
- **`feepaid.py`**: Sends confirmation emails to students who have paid their fees.

