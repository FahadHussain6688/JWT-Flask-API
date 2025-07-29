from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Configure JWT Secret Key
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production

jwt = JWTManager(app)

# Dummy user
users = {
    "admin": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(token=access_token), 200
    return jsonify({"msg": "Invalid username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {current_user}! You have access to this protected route."})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "JWT-secured Flask API is running."})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
