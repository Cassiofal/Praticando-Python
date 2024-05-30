'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
'''
def multiplicador_de_numeros(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar

duplicar = multiplicador_de_numeros(2)
triplicar = multiplicador_de_numeros(3)
quaduplicar = multiplicador_de_numeros(4)

print(duplicar(2))
print(triplicar(2))
print(quaduplicar(2))

