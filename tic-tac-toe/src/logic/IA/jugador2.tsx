import axios from 'axios';

let respuesta: any;

export async function sendMove1(board: any, playerPosition: any) {
    
    try {
        const response = await axios.post('http://localhost:5000/move1', {
            board: board,
            player_position: playerPosition
        });
       return respuesta = response.data; 
    } catch (error) {
        console.error('Error al enviar el movimiento:', error);
    }
} 

export async function sendMove2(board: any, playerPosition: any) {
    
    try {
        const response = await axios.post('http://localhost:5001/move2', {
            board: board,
            player_position: playerPosition
        });
       return respuesta = response.data; 
    } catch (error) {
        console.error('Error al enviar el movimiento:', error);
    }
} 

