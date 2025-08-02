# 🔐 Flask JWT API

A minimal Flask API secured with JWT authentication and containerized using Docker.

## 📁 Project Structure

- `app.py` — Main Flask application with JWT logic  
- `requirements.txt` — Python dependencies  
- `Dockerfile` — Docker setup to containerize the app  
- `test_api.http` — HTTP requests for local testing  

## 🐳 How to Run with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t flask-jwt-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 5000:5000 flask-jwt-app
   ```

3. **Access the API**:
   http://localhost:5000/status

## 🔐 How JWT Is Used

- POST to `/login` with username and password  
- Get a JWT token in response  
- Use `Authorization: Bearer <token>` for `/protected` route  

## ✅ Example Endpoints

| Method | Endpoint     | Description                      |
|--------|--------------|----------------------------------|
| GET    | /status      | Check if API is running          |
| POST   | /login       | Returns JWT on correct login     |
| GET    | /protected   | JWT-protected route              |

