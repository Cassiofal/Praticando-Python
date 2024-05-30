'''
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas pedem recever valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam Nome (nada)

'''
# Declara uma função e  entre parênteses determina um parâmetro (não é obrigatório)
def imprimir(nome= 'Sem nome'):# = 'valor' é utilizapa para quando a função não tiver um argumento.
    print(f'Como vai {nome}?')

# Utilização da função e entres parênteses os agumentos. Os argumentos podem ser mudatos 
#sempre que a função for utilizada.

imprimir('Roberval')    
imprimir('Rodolfo')    
imprimir('Roberto')    
imprimir('Marcinho')    
imprimir()    