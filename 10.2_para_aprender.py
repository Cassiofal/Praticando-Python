'''
Escreva uma função chamada criar_acrescentador que recebe 
um valor como parâmetro e retorna uma função interna que 
acrescenta esse valor a um número fornecido.
Por exemplo:
'''

def criar_acrescentador(acrescentador):
    def acrescentado(numero):
        return numero + acrescentador
    return acrescentado

numero_acrescentado_1 = criar_acrescentador(1)
numero_acrescentado_2 = criar_acrescentador(3)
numero_acrescentado_3 = criar_acrescentador(2)

print(numero_acrescentado_1(1))
print(numero_acrescentado_2(2))
print(numero_acrescentado_3(3))