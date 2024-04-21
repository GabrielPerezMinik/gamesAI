import { spawn } from 'child_process';
import { getBoard, getTurn } from '../../App';


// Variable que quieres enviar a Python
const myData = { turno: getTurn(),
                 tablero: getBoard() };

// Convertir el objeto JavaScript a JSON
const jsonData = JSON.stringify(myData);

// Ejecutar el script de Python y pasarle los datos como argumentos de línea de comandos
const pythonProcess = spawn('python3', ['Datos.py', jsonData]);

// Capturar la salida del proceso de Python
pythonProcess.stdout.on('data', (data) => {
  console.log(`Python script output: ${data}`);
});

// Manejar errores de ejecución del proceso de Python
pythonProcess.on('error', (error) => {
  console.error(`Error ejecutando el script de Python: ${error.message}`);
});