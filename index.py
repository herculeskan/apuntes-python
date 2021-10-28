import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('ganaste AAAAAAAAAAAA')

if __name__ == '__main__':
    run()