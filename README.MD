
## Overview

The Laundromat project is a web application designed to streamline laundry service management. It allows users to place orders, manage their accounts, and provides administrative functionality to oversee orders and users. Built using Flask for the backend and SQLite for the database, this project showcases essential features for a laundry service application.

## Features

- **User Registration & Login**: Users can create accounts and log in securely.
- **Order Management**: Users can place, view, and track their laundry orders.
- **Admin Dashboard**: Administrators can manage user accounts, view orders, and update order statuses.
- **Email Notifications**: Users receive email updates regarding their order status.
- **Responsive Design**: The application is designed to work on various devices.

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite
- **Email Service**: SMTP (Google Mail)
- **Frontend**: HTML, CSS, Bootstrap 
- **Authentication**: Flask-Login

## Frontend Inspiration

The frontend design was inspired by a pre-existing template, providing a polished and user-friendly interface for users and administrators.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CovetingAphid3/laundromat.git
   cd laundromat
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv env
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory with the following variables:

   ```
   FLASK_SECRET_KEY=your_secret_key
   DB_CONNECTION_STRING=your_database_connection_string
   EMAIL_USER=your_email@example.com
   EMAIL_PASS=your_email_password
   ```

### Running the Application

1. Initialize the database (if necessary):

   ```bash
   python3 run.py
   ```

2. Start the Flask application:

   ```bash
   flask run
   ```

3. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

### Creating an Admin User

To create an admin user, you can use the SQLite CLI:

1. Open the SQLite CLI:

   ```bash
   sqlite3 site.db
   ```

2. Insert an admin user:

   ```sql
   INSERT INTO user (name, surname, email, password, is_admin, date_created) VALUES ('admin', 'admin', 'admin@example.com', 'your_hashed_password', 1, CURRENT_TIMESTAMP);
   ```

3. Verify the insertion:

   ```sql
   SELECT * FROM user WHERE email = 'admin@example.com';
   ```

### Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
