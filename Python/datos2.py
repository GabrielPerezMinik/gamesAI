from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/move": {"origins": "http://localhost:5000"}})
@app.route('/move', methods=['POST'])
def handle_move():
    data = request.json
    # Aquí puedes procesar los datos recibidos y realizar cualquier acción necesaria.
    # Por ejemplo, puedes acceder al tablero y la posición del jugador como data['board'] y data['player_position']
    print("Tablero recibido:", data['board'])
    print("Posición del jugador recibida:", data['player_position'])
    # Aquí puedes enviar una respuesta si es necesario

    return  jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
