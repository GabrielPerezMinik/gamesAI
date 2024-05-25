from flask import Flask, request
from flask_cors import CORS
from IA3EnrayaAlgoritmo import find_best_move


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/move": {"origins": "http://localhost:5173"}})
@app.route('/move', methods=['POST'])
def handle_move():
    
    data = request.json


    best_move = find_best_move(data['board'])
    data['board'][best_move] = '⚪'
    return data


if __name__ == '__main__':
    app.run(debug=True)