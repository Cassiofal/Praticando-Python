'''
Aula 107
Valores padrão para parâmetros
Ao definir um função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
'''
# não pode ser utilizado z=0 porque sempre retornará false
def soma(x, y, z=None):
    # Caso haja qualquer valor que não for None o if será execultado 
    if z is not  None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)  

soma(1, 2,)
# Não é None, pois o z recebeu o valar 0.
soma(1, 2, 0)
