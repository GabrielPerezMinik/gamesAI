import { useState } from 'react'
import { Square } from './components/Square.jsx'
import { TURNS } from './constants.js'
import { checkWinnerFrom, checkEndGame } from './logic/board.js'
import { WinnerModal } from './components/WinnerModal.jsx'
import { saveGameToStorage, resetGameStorage } from './logic/storage/index.js'
import confetti from "canvas-confetti"
import { sendMove1, sendMove2} from './logic/IA/jugador2.tsx'



function App () {

  const [gameStarted, setGameStarted] = useState(false)
  const [difficulty, setDifficulty] = useState(null)

  const [board, setBoard] = useState(() => {
    const boardFromStorage = window.localStorage.getItem('board')
    if (boardFromStorage) return JSON.parse(boardFromStorage)
    return Array(9).fill(null)
  })

  const [turn, setTurn] = useState(() => {
    const turnFromStorage = window.localStorage.getItem('turn')
    return turnFromStorage ?? TURNS.X
  })

  // null es que no hay ganador, false es que hay un empate
  const [winner, setWinner] = useState(null)

  const resetGame = () => {
    setBoard(Array(9).fill(null))
    setTurn(TURNS.X)
    setWinner(null)


    resetGameStorage()
  }


  const newTurn = turn;

  const newBoard = [...board];

  const updateBoard = async (index) => {
    if(turn == TURNS.X){
    // no actualizamos esta posición
    // si ya tiene algo
    if (board[index] || winner) return
    // actualizar el tablero
    const newBoard = [...board]
    newBoard[index] = turn
    
    setBoard(newBoard)
    // cambiar el turno a la IA
    const newTurn = turn === TURNS.X ? TURNS.O : TURNS.X
    setTurn(newTurn)
    // guardar aqui partida
    saveGameToStorage({
      board: newBoard,
      turn: newTurn
    })
    // revisar si hay ganador
    let newWinner = checkWinnerFrom(newBoard)
    if (newWinner) {
      confetti()
      setWinner(newWinner)
      return;
    } else if (checkEndGame(newBoard)) {
      setWinner(false) // empate
      return;
    }
    // movimiento de la IA
    let valorIA;

    // IA poco entrenada
    
    if(difficulty == "facil"){ 
      valorIA = await sendMove1(newBoard, newTurn);
    }

    // IA imposible de ganar
    
    if(difficulty == "dificil"){
      valorIA = await sendMove2(newBoard, newTurn);
    }
    
    // actualizar el tablero IA
    setBoard(valorIA.board)
    // guardar aqui partida IA
    saveGameToStorage({
      board: valorIA.board,
      turn: valorIA.turn
    })
    // revisar si hay ganador IA
    newWinner = checkWinnerFrom(valorIA.board)
    if (newWinner) {
      confetti()
      setWinner(newWinner)
    } else if (checkEndGame(valorIA.board)) {
      setWinner(false) // empate
    }
    // cambiar el turno al jugador
    setTurn(TURNS.X)
    }
  }

  if (!gameStarted) {
    return (
      <div className='dificultad' onLoad={resetGameStorage()}>
        <h1>Elige la dificultad</h1>
        <button onClick={() => { setDifficulty('facil'); setGameStarted(true); }} className='boton-dificultad'>Fácil</button>
        <button onClick={() => { setDifficulty('dificil'); setGameStarted(true); }} className='boton-dificultad'>Difícil</button>
      </div>
    )
  }
  return (
    
    <main className='board'>
      <h1>Tic tac toe</h1>
      <button onClick={resetGame}>Reset del juego</button>
      <section className='game'>
        {
          board.map((square, index) => {
            return (
              <Square
                key={index}
                index={index}
                updateBoard={updateBoard}
              >
                {square}
              </Square>
            )
          })
        }
      </section>

      <section className='turn'>
        <Square isSelected={turn === TURNS.X}>
          {TURNS.X}
        </Square>
        <Square isSelected={turn === TURNS.O}>
          {TURNS.O}
        </Square>
      </section>

      <WinnerModal resetGame={resetGame} winner={winner} />
    </main>
  )
}
export default App 
