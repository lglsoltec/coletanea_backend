from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite chamadas do app Flutter

# Simula um banco de dados simples com e-mails cadastrados
usuarios = set()

@app.route("/")
def home():
    return "Backend Coletânea Digital funcionando com sucesso!"

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "E-mail é obrigatório"}), 400

    if email in usuarios:
        return jsonify({"message": "E-mail já cadastrado"}), 200

    usuarios.add(email)
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 200

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "E-mail é obrigatório"}), 400

    if email not in usuarios:
        return jsonify({"error": "E-mail não encontrado"}), 401

    return jsonify({"message": "Login bem-sucedido!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
