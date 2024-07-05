
This is a Flask application that provides a REST API for CRUD operations on user data, stored in a MongoDB database. The application is containerized using Docker for easy setup and deployment.

## Prerequisites

- Docker
- Docker Compose
- Postman (for testing the API)

## Setup and Running the Application

1. Clone the repository
2. Make sure you have the following files in your project directory:
- `app.py`: The Flask application
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Defines and runs the multi-container Docker application

3. Build and start the Docker containers:
 
 "docker-compose up --build"

This command will build the Docker image for the Flask app and start both the Flask app and MongoDB containers.

4. The application should now be running and accessible at `http://localhost:5000`.

## API Endpoints

- `GET /users`: Retrieve all users
- `GET /users/<id>`: Retrieve a specific user by ID
- `POST /users`: Create a new user
- `PUT /users/<id>`: Update an existing user
- `DELETE /users/<id>`: Delete a user

## Testing the API

You can use Postman to test the API endpoints. Here are some example requests:

1. Create a new user (POST request to `http://localhost:5000/users`):

 "{ 
  "name": "test",
  "email": "test3030@gmail.com",
  "password": "test"
}"

2. Get all users (GET request to http://localhost:5000/users)
3. Get a specific user (GET request to http://localhost:5000/users/<user_id>)
4. Update a user (PUT request to http://localhost:5000/users/<user_id>):

 "{ 
  "name": "test2",
  "email": "test3030@gmail.com2",
  "password": "test2"
}"

5. Delete a user (DELETE request to http://localhost:5000/users/<user_id>)

