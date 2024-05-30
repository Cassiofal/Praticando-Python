'''
Exercícios com função

Crie uma função que multiplica todos so argumentos
não noeados recebido
Retorne o taltal para um variável e mostre o valor
da variável.

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
'''

# Empacota parametro não nomeado
def multiplicacao(*args):
    total = 1
    for n in args:
        total *= n
        
    return total

multiplicacoes = multiplicacao(20, 10, 33, 5)

print(multiplicacoes)

def par_primpar(x):
    multiplo_de_dois = x % 2 == 0
    # Caso o número for multiplo de 2, retorna o número como True
    if multiplo_de_dois:
        return  f"O Número {multiplicacoes} é par."
    # retorna o resulatado caso o número NÃO for multiplo de dois, não sendo necessário o else
    return f"O número {multiplicacoes} é ímpar."
       
            
print(par_primpar(multiplicacoes))
