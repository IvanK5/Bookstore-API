# **Bookstore API**

This simple Bookstore API is built using **FastAPI** and **SQLAlchemy** for managing books. The API allows users to add, update, delete, and retrieve books stored in a database.

## **Table of Contents**
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Database Setup](#database-setup)
5. [Running the API](#running-the-api)
6. [API Endpoints](#api-endpoints)
7. [Testing the API](#testing-the-api)
8. [Using Your Own Database](#using-your-own-database)
9. [Contributing](#contributing)

---

## **Features**

- Add new books to the database
- Retrieve a list of all books
- Retrieve details of a single book
- Update book information
- Delete a book

## **Requirements**

- Python 3.10 or higher
- FastAPI
- SQLAlchemy
- Uvicorn (for running the development server)
- Pydantic (for data validation)

## **Installation**

1. **Clone the repository:**

`git clone https://github.com/IvanK5/Bookstore-API.git` 
   
2. **Create and activate a virtual environment:**

`python -m venv venv` 

 `source venv/bin/activate`  # On Windows: `venv\Scripts\activate`

3. **Install the required dependencies:**

`pip install -r requirements.txt`

## **Database Setup**

By default, the API uses SQLite as its database. If you want to use your own database, follow the steps in the Using Your Own Database section.

To create the initial database and tables, run the following command after installation:

``python app/main.py``

## **Running the API**

``uvicorn app.main:app --reload``

The API will be available at http://127.0.0.1:8000.

You can access the auto-generated API documentation via:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

## **API Endpoints**

Here is a list of the available API endpoints:

GET /books/ - Retrieve a list of all books
GET /books/{book_id} - Retrieve a specific book by its ID
POST /books/ - Add a new book
PUT /books/{book_id} - Update details of an existing book
DELETE /books/{book_id} - Delete a book

## **Testing the API**

To test the API, you can use tools like:

Curl: Command-line tool for making HTTP requests
Postman: GUI tool for testing API endpoints
Swagger UI: Use the built-in API documentation at /docs to test each endpoint directly from the browser.

## **Using Your Own Database**

If you have an existing database (e.g., MySQL, PostgreSQL), you can configure the database settings in the app/database.py file. Change the SQLALCHEMY_DATABASE_URL to match your own database connection string.

Example for PostgreSQL:

``SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"``

Then, run the migrations to create the necessary tables:

``python app/main.py``

