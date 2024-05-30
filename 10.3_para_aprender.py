'''
Escreva uma função chamada criar_contador que retorna 
uma função interna. Cada vez que a função interna é 
chamada, ela deve incrementar e retornar um contador.
'''

def criar_contador(conto):
    def contador(numero):
        total = 0
        for n in conto: 
            total = n + 1
        return total
    return contador

conta = criar_contador()
print(conta())
print(conta())
print(conta())
print(conta())

        