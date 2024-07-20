import os
from playsound import playsound
import time
import random


mensagem = []
nome = input("Nome: ")

while True:
    os.system('clear')
    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])
    print("__________________________________________________")
    texto = input("mensagem: ")
    if texto == '/sair':
        break
    if texto == '/senhas':
        import teste
    if texto == "/limpar": 
        os.system('clear')
    if texto == '/random':
        print(1)
    elif texto == '/peido':
        playsound('/home/mikaritos/Documentos/Programa/python project/Mini chat/fart.mp3')
    elif texto == '/creeper':
        print(':::::::      :::::::')
        print(':::::::      :::::::')
        print(':::::::      :::::::')
        print(':::::::      :::::::')
        print('       :::::: ')
        print('       :::::: ')
        print('   ::::::::::::::')
        print('   ::::::::::::::')
        print('   ::::::::::::::')
        print('   ::::      ::::')
        print('   ::::      ::::')
        playsound('/home/mikaritos/Documentos/Programa/python project/Mini chat/creeper.mp3')            
    if texto == "/calcular":
        operador = input("Quais tipos de operação?: + - * /")
        if operador == '/sair' or texto == '/sair':
            break
        if operador == '+' or operador == '-' or operador == '*' or operador == '/':
             x = float(input('Primeiro valor: '))
             y = float(input('Segundo valor: '))

        if operador == '+': resultado = x + y
        if operador == '-': resultado = x - y
        if operador == '*': resultado = x * y
        if operador == '/': resultado = x / y
        produto = round(resultado, 2)
        print(produto)
    
        input("precione ENTER para continuar")
        os.system('clear')
    
    mensagem.append({
        "nome": nome.title(),
        "texto": texto.title(),
    })

#sintaxe "lower" transformara texto em minusculo
#sintaxe "title" tenforma as primeiras letras em maiuscolas