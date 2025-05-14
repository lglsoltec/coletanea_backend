from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend Coletânea Digital funcionando com sucesso!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    # Lógica simplificada (substitua por validação real)
    if email:
        return jsonify({'success': True})
    return jsonify({'success': False}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    # Lógica simplificada
    if email:
        return jsonify({'success': True})
    return jsonify({'success': False}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
