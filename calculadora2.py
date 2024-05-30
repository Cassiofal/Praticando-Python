# Primerio eu defini as funções somar, subtrar, etc. para utiliza-las mais tarde
def soma(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
# Previne que o usuário tente dividir qualquer número por 0.
def division(x, y):
    if y == 0:
        return 'Falha na divisão'
    return x / y
# Enquanto for verdade o código se repete
# Apenas deixara de ser verdade quando todo código for executado e quanquer 
# coisa que não for s for digitada pelo usuário
while True:

    choices = input("Escola uma opção\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n:")
    # Qualquer coisa que não for um número de 1 a 4 entrará no else
    if choices in ['1', '2', '3', '4']:
        number1 = float(input("Digite um Numero: "))
        number2 = float(input("Digite outro Numero: "))

        if choices == '1':
            print(f'{number1} + {number2} = {soma(number1, number2)}')
        elif choices == '2':
            print(f'{number1} - {number2} = {sub(number1, number2)}')
        elif choices == '3':
            print(f'{number1} * {number2} = {mult(number1, number2)}')
        elif choices == '4':
            print(f'{number1} / {number2} = {division(number1, number2)}')

    else:
        print("Comando inválido")
    # Essa variável está fora do escopo do else
    # Ela é execultada sempre que o calculo terminar ou quando algo que não for um
    # número s
    # de 1 a 4 for lido como entrada nas opções.
    continue_or_not = input("Deseja calcular outros números? \n[S]im \n[N]ão\n:")
    # Para o programa caso entre qualquer coisa que não for um 's'.
    if continue_or_not.lower() != 's':
        print("End of operation.")
        break

