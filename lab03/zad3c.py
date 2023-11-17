import pickle
import os
import json

def resultFormat(format='pickle'):
    def decorator(func):
        filePath = 'result.' + format

        def wrapper(*args, **kwargs):
            if os.path.exists(filePath):
                with open(filePath, 'rb' if format == 'pickle' else 'r') as file:
                    if format == "pickle":
                        result = pickle.load(file)
                    if format  == "json":
                        result = json.load(file)
                print(f"Wynik wczytany z pliku: {filePath}")
            else:
                result = func(*args, **kwargs)
                with open(filePath, 'wb' if format == 'pickle' else 'w') as file:
                    if format == "pickle":
                        pickle.dump(result, file)
                    if format == "json":
                        json.dump(result, file)
                print(f"Wynik zapisany do pliku: {filePath}")

            return result
        return wrapper
    return decorator

@resultFormat(format='json')
def evenOdd(a):
    if (a % 2 == 0):
        return True
    else:
        return False

result1 = evenOdd(7)
print("Wynik 1:", result1)