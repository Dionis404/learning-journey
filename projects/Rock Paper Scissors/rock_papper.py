import random

z = int(input('Выбери: \n1-Камень \n2-Ножницы \n3-Бумага \n'))
if z == 1: 
    z = 'Камень'
elif z == 2:
    z = 'Ножницы'
elif z == 3:
    z = 'Бумага'

x = ["Камень", "Ножницы","Бумага"]
y = random.choice(x)

if y == "Камень" and z == 'Камень':
    print('Ничья')
elif y == "Ножницы" and z == 'Камень':
    print('Победа')
elif y == "Бумага" and z == 'Камень':
    print('Проигрыш')

if y == "Камень" and z == 'Ножницы':
    print('Проигрыш')
elif y == "Ножницы" and z == 'Ножницы':
    print('Ничья')
elif y == "Бумага" and z == 'Ножницы':
    print('Победа')
    

if y == "Камень" and z == 'Бумага':
    print('Победа')
elif y == "Ножницы" and z == 'Бумага':
    print('Проигрыш')
elif y == "Бумага" and z == 'Бумага':
    print('Ничья')
    