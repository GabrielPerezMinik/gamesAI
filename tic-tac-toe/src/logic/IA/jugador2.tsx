import axios from 'axios';

let respuesta: any;

export async function sendMove(board: any, playerPosition: any) {
    
    try {
        const response = await axios.post('http://localhost:5000/move', {
            board: board,
            player_position: playerPosition
        });
       return respuesta = response.data; 
    } catch (error) {
        console.error('Error al enviar el movimiento:', error);
    }
} 

