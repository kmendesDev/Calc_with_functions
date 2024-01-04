import os
num1 = 0
num2 = 0
result = 0
op = None

def Menu():
    os.system('clear')
    print('Menu principal - Calculadora \n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    op = input('\nInforme qual a operação matemática que você deseja realizar: ')
    if op == '1':
        os.system('clear')
        print("Você selecionou SOMA: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))    
        soma(num1,num2)
    elif op == '2':
        os.system('clear')
        print("Você selecionou SUBTRAÇÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))    
        subt(num1,num2)
    elif op == '3':
        os.system('clear')
        print("Você selecionou MULTIPLICAÇÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))    
        multip(num1,num2)
    elif op == '4':
        os.system('clear')
        print("Você selecionou DIVISÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))    
        div(num1,num2)
    else:
        os.system('clear')
        print('Programa Finalizado. Até breve !\n')
        return

def soma(num1,num2):
    os.system('clear')
    result = num1+num2
    print(f'\n Resultado: {num1}+{num2} = {result}\n')
    print('Menu da soma: \n')
    print('1 - Retornar ao menu principal ')
    print('2 - Realizar nova soma com 2 números novos ')    
    print('3 - Somar um número ao resultado ')
    print('4 - Subtrair o resultado de um novo número: ')
    print('5 - Multiplicar o resultado por um novo número: ')
    print('6 - Dividir o resultado por um novo número: ')
    print('7 - Sair')
    
    op = input('\nDigite a opção: ')
    
    if op=='1':
        Menu()
    if op=='2':
        os.system('clear')
        print("SOMA: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número:  '))    
        soma(num1,num2)  
    if op=='3':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para somar com {result}: '))
        soma(result,num2)
    if op=='4':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para subtrair de {result}: '))
        subt(result,num2)        
    if op=='5':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para multiplicar com {result}: '))
        multip(result,num2)
    if op=='6':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para dividir de {result}: '))
        div(result,num2)
    else:
        os.system('clear')
        print('Programa Finalizado. Até breve !\n')
        return
    

def subt(num1,num2):
    os.system('clear')
    result = num1-num2
    print(f'\n Resultado: {num1}-{num2} = {result}\n')
    print('Menu da subtração: \n')
    print('1 - Retornar ao menu principal ')
    print('2 - Realizar subtração com 2 números novos ')    
    print('3 - Somar um número ao resultado ')
    print('4 - Subtrair o resultado de um novo número: ')
    print('5 - Multiplicar o resultado por um novo número: ')
    print('6 - Dividir o resultado por um novo número: ')
    print('7 - Sair')

    op = input('\nDigite a opção: ')

    if op=='1':
        Menu()
    if op=='2':
        os.system('clear')
        print("SUBTRAÇÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número:  '))    
        subt(num1,num2)  
    if op=='3':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para somar com {result}: '))
        soma(result,num2)
    if op=='4':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para subtrair de {result}: '))
        subt(result,num2)        
    if op=='5':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para multiplicar com {result}: '))
        multip(result,num2)
    if op=='6':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para dividir de {result}: '))
        div(result,num2) 
    else:
        os.system('clear')
        print('Programa Finalizado. Até breve !\n')
        return
    
def multip(num1,num2):
    os.system('clear')
    result = num1*num2
    print(f'\n Resultado: {num1}x{num2} = {result}\n')
    print('Menu da multiplicação: \n')
    print('1 - Retornar ao menu principal ')
    print('2 - Realizar multiplicação com 2 números novos ')    
    print('3 - Somar um número ao resultado ')
    print('4 - Subtrair o resultado de um novo número: ')
    print('5 - Multiplicar o resultado por um novo número: ')
    print('6 - Dividir o resultado por um novo número: ')
    print('7 - Sair')

    op = input('\nDigite a opção: ')

    if op=='1':
        Menu()
    if op=='2':
        os.system('clear')
        print("MULTIPLICAÇÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número:  '))    
        multip(num1,num2)  
    if op=='3':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para somar com {result}: '))
        soma(result,num2)
    if op=='4':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para subtrair de {result}: '))
        subt(result,num2)        
    if op=='5':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para multiplicar com {result}: '))
        multip(result,num2)
    if op=='6':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para dividir de {result}: '))
        div(result,num2)
    else:
        os.system('clear')
        print('Programa Finalizado. Até breve !\n')
        return
    
def div(num1,num2):
    os.system('clear')
    result = num1/num2
    print(f'\n Resultado: {num1}/{num2} = {result}\n')
    print('Menu da divisão: \n')
    print('1 - Retornar ao menu principal ')
    print('2 - Realizar divisão com 2 números novos ')    
    print('3 - Somar um número ao resultado ')
    print('4 - Subtrair o resultado de um novo número: ')
    print('5 - Multiplicar o resultado por um novo número: ')
    print('6 - Dividir o resultado por um novo número: ')
    print('7 - Sair')

    op = input('\nDigite a opção: ')

    if op=='1':
        Menu()
    if op=='2':
        os.system('clear')
        print("DIVISÃO: \n")
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número:  '))    
        div(num1,num2)  
    if op=='3':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para somar com {result}: '))
        soma(result,num2)
    if op=='4':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para subtrair de {result}: '))
        subt(result,num2)        
    if op=='5':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para multiplicar com {result}: '))
        multip(result,num2)
    if op=='6':
        os.system('clear')
        num2 = int(input(f'\nDigite o número para dividir de {result}: '))
        div(result,num2)
    else:
        os.system('clear')
        print('Programa Finalizado. Até breve !\n')
        return

#Iniciando a calculadora: 
Menu()



    