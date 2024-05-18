from flask import Flask, request, jsonify
from flask_cors import CORS
from IATicTacToe import ia_movimiento
from IA3EnrayaConvolucional import make_move
import numpy as np

def desencript(data):
   
    for i in range(len(data['board'])):
        if data['board'][i] == '❌':
            data['board'][i] = '2'
        elif data['board'][i] == '⚪':
         data['board'][i] = '1'

    return data


def encript(data):
    for i in range(len(data['board'])):
        if data['board'][i] == '2':
            data['board'][i] = '❌'
        elif data['board'][i] == '1':
            data['board'][i] = '⚪'
    return data

def tunelaIA(data):

    zeros_array = np.zeros((3, 3))

    for i, value in enumerate(data):
        if value is not None:
            zeros_array[i // 3, i % 3] = value

    return zeros_array

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/move": {"origins": "http://localhost:5173"}})
@app.route('/move', methods=['POST'])
def handle_move():
    data = request.json
    # Aquí puedes procesar los datos recibidos y realizar cualquier acción necesaria.
    # Por ejemplo, puedes acceder al tablero y la posición del jugador como data['board'] y data['player_position']
    #print("Tablero recibido:", data['board'])
    #print("Posición del jugador recibida:", data['player_position'])
    
    
    #print(data)
    # Aquí puedes enviar una respuesta si es necesario

    #data['board'][2] = '⚪'

    data2=desencript(data)

    board=tunelaIA(data2['board'])
            
    move=make_move(board)    


    #data2['board'][make_move(board)]='0'

    data2['board'][move]='1'

   
    #while data2['board'][move]=='0':
        
    #    move=make_move(board)
    #    data2['board'][move]='0'
    print(move)
    
    #print(data2)
    print(encript(data2))

    #print(data)
    #movimiento=ia_movimiento(data2['board'])

    #print(data2['board'])
    #print(movimiento)


    return data2

if __name__ == '__main__':
    app.run(debug=True)