TARGET_NUMBER = 87
number = 0
num_tries = 0
while number != TARGET_NUMBER:
    number = int(input('TECLEE UN NÚMERO: '))
    num_tries += 1
    if number > TARGET_NUMBER:
        print('EL NÚMERO TIENE QUE SER MENOR')
    elif number < TARGET_NUMBER:
        print('EL NÚMERO TIENE QUE SER MAYOR')
    else:
        print(f'✅ ¡ENHORABUENA! HAS ENCONTRADO EL NÚMERO EN {num_tries} INTENTOS')
        break