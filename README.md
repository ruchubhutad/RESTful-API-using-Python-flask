# RESTful-API-using-Python-flask
Building RESTful APIs using Python and interacting with databases.

This is a RESTful API built using Flask for managing products in an e-commerce application.

Setup
Prerequisites
Python 3.x installed on your system.
Flask and Flask-SQLAlchemy installed. You can install them via pip:
bash

pip install Flask Flask-SQLAlchemy
Installation
Clone this repository to your local machine:
bash

git clone https://github.com/yourusername/e-commerce-api.git
Navigate to the project directory:
bash

cd e-commerce-api
Initialize the SQLite database:
bash

python
from app import db
db.create_all()
exit()
Running the API
To run the API, execute the following command in your terminal:

bash

python app.py
The API will start running on http://127.0.0.1:5000/.

Endpoints
GET /products: Retrieve a list of all products.
GET /products/{id}: Retrieve details of a specific product by its ID.
POST /products: Create a new product.
PUT /products/{id}: Update an existing product by its ID.
DELETE /products/{id}: Delete a product by its ID.
Usage
You can use tools like Postman or send requests directly from your Python code to interact with the API.

Example request to retrieve all products:

bash

curl http://127.0.0.1:5000/products
Example request to retrieve details of a specific product:

bash

curl http://127.0.0.1:5000/products/1
Unit Tests
Unit tests are provided in the tests directory. You can run them using pytest:

bash

pytest tests

