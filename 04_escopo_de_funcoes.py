'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
Oescopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
'''

# Observação: Uma função só pode usar uma variável que esta a cima dela, mas nunca uma abaixo
x = 1

def escopo():
    #Caso a variável x não foce definida na função ela seria utilizado a variável x que está a cima da função 
    x = 10

    def outra_funcao():
        y = 2
        # O x utilizado é o da função escopo porque ele está a cima
        print(y, x)
    # Chama outra_funcao tentra fa função escopo
    outra_funcao()
    # x da própria função escopo
    print(x)

print(x)
escopo()
print(x)