import sys
import json

# Leer los datos pasados como argumentos de línea de comandos
received_data = sys.argv[1]

# Convertir JSON a diccionario Python
data_dict = json.loads(received_data)

# Hacer algo con los datos
print("Python script received:", data_dict)
