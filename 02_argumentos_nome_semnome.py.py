'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    #Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y = ', x + y + z)

soma(1, 2, 3)
soma(1, 2, z=3)
# Sempre que um argumento for nomeado todos ou demais devem ser nomeados também.   
soma(1, y=2, z=3)   
print(1, 2, 3, sep='-')   