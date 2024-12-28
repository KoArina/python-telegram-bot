import random
import json1

data = None

try:
    with open('text.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print('файл відсутній створюєм новий')
    with open ('text.txt', 'w') as file:
        file.write('по замовчуванню . . .')
finally:
    if not data:
        with open('text.txt', 'r') as file:
            data = file.read()

print(data)