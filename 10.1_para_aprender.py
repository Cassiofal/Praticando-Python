'''
Escreva uma função chamada criar_potencia que recebe um expoente 
como parâmetro e retorna uma função interna que calcula a potência 
de um número fornecido.
Por exemplo:
'''

def criar_potencia(potencia):
    def numeros(numero):
        return numero ** potencia    
    return numeros

quadrado = criar_potencia(2)
cubo = criar_potencia(3)

print(quadrado(2))
print(cubo(2))