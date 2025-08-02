# Flask JWT API

## Project Structure

- `app.py`: Main Flask application with JWT authentication.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Container setup for running the app.
- `test_api.http`: Example HTTP requests for testing the API.

## How to Run with Docker

1. Build the Docker image:
   ```sh
   docker build -t flask-jwt-app .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 flask-jwt-app
   ```
3. The API will be available at `http://localhost:5000`.

## How JWT Is Used

- Users log in via `/login` with a username and password.
- On successful login, a JWT token is returned.
- Protected routes (like `/protected`) require the JWT token in the `Authorization: Bearer <token>` header.
- The token is verified using the secret key