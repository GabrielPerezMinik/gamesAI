def check_winner(board):
    # Definimos las combinaciones ganadoras
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] is not None:
            return board[combo[0]]
    
    return None

def is_full(board):
    return all(spot is not None for spot in board)

def evaluate(board):
    winner = check_winner(board)
    if winner == '❌':
        return 1
    elif winner == '⚪':
        return -1
    else:
        return 0

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot is None]

def minimax(board, depth, is_maximizing_player, alpha, beta):
    score = evaluate(board)
    
    # Si el juego ha terminado, devolver la puntuación
    if score == 1 or score == -1:
        return score
    
    if is_full(board):
        return 0
    
    if is_maximizing_player:
        best = -float('inf')
        for move in get_available_moves(board):
            board[move] = '❌'
            best = max(best, minimax(board, depth + 1, False, alpha, beta))
            board[move] = None
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for move in get_available_moves(board):
            board[move] = '⚪'
            best = min(best, minimax(board, depth + 1, True, alpha, beta))
            board[move] = None
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def find_best_move(board):
    best_val = float('inf')
    best_move = -1
    
    for move in get_available_moves(board):
        board[move] = '⚪'
        move_val = minimax(board, 0, True, -float('inf'), float('inf'))
        board[move] = None
        
        if move_val < best_val:
            best_move = move
            best_val = move_val
    
    return best_move
