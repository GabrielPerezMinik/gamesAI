import sys
import json

received_data = sys.argv[0]


data_dict = json.loads(received_data)


print("Python script received:", data_dict)
