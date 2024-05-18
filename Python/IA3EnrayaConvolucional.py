import numpy as np
import tensorflow as tf

# Definir la red neuronal convolucional
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(3, 3, 1)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(9, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Función para generar datos de entrenamiento
def generate_data():
    X_train = []
    y_train = []
    for i in range(1000):
        board = np.zeros((3, 3))
        moves = np.random.randint(0, 9, np.random.randint(1, 6))
        for move in moves:
            row = move // 3
            col = move % 3
            if board[row, col] == 0:
                board[row, col] = 1
        X_train.append(board.reshape((3, 3, 1)))
        available_moves = np.where(board.flatten() == 0)[0]
        y_train.append(np.random.choice(available_moves))
    return np.array(X_train), np.array(y_train)

# Generar datos de entrenamiento
X_train, y_train = generate_data()

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10)

# Función para que la IA haga un movimiento
def make_move(board):
    board = board.reshape((1, 3, 3, 1))
    prediction = model.predict(board)[0]
    available_moves = np.where(board.flatten() == 0)[0]
    available_predictions = [prediction[i] for i in available_moves]
    move = available_moves[np.argmax(available_predictions)]
    return move

# Ejemplo de cómo la IA haría un movimiento
current_board = np.array([[0, 0, 0],
                          [0, 1, 0],
                          [0, 0, 0]])
#move = make_move(current_board)
#print("La IA hace su movimiento en la posición:", move)
