from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simula um "banco de dados" com e-mail e senha
usuarios = {}

@app.route("/")
def home():
    return "Backend Coletânea Digital funcionando com sucesso!"

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    senha = request.form.get("password")

    if not email or not senha:
        return jsonify({"error": "E-mail e senha são obrigatórios"}), 400

    if email in usuarios:
        return jsonify({"message": "E-mail já cadastrado"}), 200

    usuarios[email] = senha
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 200

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("password")

    if not email or not senha:
        return jsonify({"error": "E-mail e senha são obrigatórios"}), 400

    if email not in usuarios:
        return jsonify({"error": "E-mail não cadastrado"}), 401

    if usuarios[email] != senha:
        return jsonify({"error": "Senha incorreta"}), 403

    return jsonify({"message": "Login bem-sucedido!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
