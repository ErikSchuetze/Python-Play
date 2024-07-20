import random

print("Sejá bem vindo, meu caro, ao gerador de senha caseiro")

## Variaveis
caracteres = "zaqwsxcderfvbgtyhnmjuiklopZAQWSXCDERFVBGTYHNMJUIKLOP1234567890!@#$%¨&*-_=+?.,><"

quant = input('Quantas senhas serão geradas? ')
quant = int(quant)

digitos = input("Quantos digitos sera necessarios? ")
digitos = int(digitos)


for sees in range(quant):
    passwords = ''
    for c in range(digitos):
        passwords += random.choice(caracteres)
    print(passwords)

input("Precione ENTER para sair")