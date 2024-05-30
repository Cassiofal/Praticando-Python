def adicao(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    if y == 0:
        return 'Erro: Divão poer zero!'
    return x / y

print('Selecione a Operação:')
print('1 Adição')
print('2 Subtração')
print('3 Multiplicação')
print('4 Divisão')

while True:
    choice = input("Digite sua escolha 1/2/3/4: ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número"))
        num2 = float(input("Digite o segundo número"))

        if choice == '1':
            print(f'{num1} + {num2} = {adicao(num1, num2)}')
        elif choice == '2':
            print(f'{num1} - {num2} = {subtracao(num1, num2)}')
        elif choice == '3':
            print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
        elif choice == '4':
            print(f'{num1} / {num2} = {divisao(num1, num2)}')
    else:
        print("Escolha invalida")

    next_calculation = input("Deseja fazer outro calculo? (s/n): ")  
    if next_calculation.lower() != 's':
        break
