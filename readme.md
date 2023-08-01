Student Registration Form using Flask and MySQL

Introduction

This project is a simple web application built with Flask that allows users to register their details in a student registration form. The form data is stored in a MySQL database.

Technologies Used

1.Flask: A micro web framework for Python.

2.MySQL: A popular open-source relational database management system.

3.HTML: For creating the frontend layout.

4.CSS: For styling the frontend elements.

Project Description: 

The Student Registration Form is a web application built using Flask, a micro web framework for Python, and MySQL, an open-source relational database management system. The application allows students to register their personal details in a form, and the data is stored in a MySQL database for later retrieval.

Features:

Registration Form: 

The application presents a simple and user-friendly registration form where students can input their name, mobile number, email, department, college name, and age.

Database Integration: 

The application uses the mysql.connector library to establish a connection to the MySQL database. Upon submitting the form, the data is inserted into the 'regform' table of the 'RAAJA' database.

Validation: 

Basic form validation is implemented to ensure that required fields are filled out before submitting the form.

Success Page: 

After successful registration, the user is redirected to a success page (success.html), confirming their registration.


Project Structure:

The project consists of the following files:


app.py: 

This is the main Python script that contains the Flask application. It handles form submission, connects to the MySQL database, and inserts form data into the 'regform' table.

index.html: 

This HTML file contains the frontend layout of the registration form. It includes input fields for name, mobile number, email, department, college name, and age. The form data is submitted to the Flask backend.

style.css: 

This CSS file provides styling for the registration form, making it visually appealing.

Setup and Execution:

Install Flask and mysql.connector using the command pip install Flask mysql-connector-python.

Ensure that MySQL is installed and running on your machine. Create a new database named 'RAAJA'.

Save the app.py, index.html, and style.css files in the same directory.

Run the Flask application by executing app.py in your terminal or command prompt using python app.py.

Access the registration form by opening a web browser and navigating to http://127.0.0.1:5000/.

Fill in the required details in the form and click the "Register" button. The data will be stored in the MySQL database.

After successful registration, the user will be redirected to the success page, confirming their registration.

Conclusion:

The Student Registration Form project showcases a basic web application using Flask and MySQL to register student details. It provides a starting point for building more complex web applications and can be extended to include additional features like login, data retrieval, and more advanced form validations.
