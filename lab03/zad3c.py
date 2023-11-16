import pickle
import os

def decorator(func):
    filePath = "result.pkl"

    def wrapper(arg):
        if os.path.exists(filePath):
            with open(filePath, 'rb') as file:
                result = pickle.load(file)
            print(f"Wynik wczytany z pliku: {filePath}")
        else:
            result = func(arg)
            with open(filePath, 'wb') as file:
                pickle.dump(result, file)
            print(f"Wynik zapisany do pliku: {filePath}")

        return result

    return wrapper

# dekorator
@decorator
def evenOdd(a):
    if (a % 2 == 0):
        return True
    else:
        return False

# Przykład użycia
result1 = evenOdd(7)
print("Wynik 1:", result1)

result2 = evenOdd(20)
print("Wynik 2:", result2)
