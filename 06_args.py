'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# Lembrete de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# recebe o argumento e empacota
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total        

soma_1_2_3 = soma(1, 2, 3)

numeros_tupla = 1, 2, 3, 4, 5, 6, 7, 83,  9
#desempaco a tupla
soma_outra = soma(*numeros_tupla)
print(soma_outra)
# Essa função soma os números, mas ela tem um limite de parámetros
# por isso o foi colocado tudo em numeros_tupla.
print(sum(numeros_tupla))
