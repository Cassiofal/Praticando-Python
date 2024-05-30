'''
Manipulando chaves e valores em dicionários
'''
# Cria um dicionário
pessoa = {}
...
...
# Adiciona uma nova chave ao dicionário pessoa 
pessoa['nome'] = 'Rodolfo Rodovico'
pessoa['sobrenome'] = 'Rivaz'
# mostra o dicionário pessoa
print(pessoa)
# mostra a chave especifica dentro no dicionário pessoa.
print(pessoa['nome'])
print()

print("chave dinamica:")
# Criando uma chave dinamica

chave = 'nome_completo'
pessoa[chave] = 'Rodolfo Rodovico'
print(pessoa[chave])
print()
# Altera o valor da chave.
pessoa[chave] = 'Maria Maranata'
print(pessoa[chave])
print(pessoa['sobrenome'])
print()
# Deleta a chave
print(pessoa)
del pessoa['sobrenome']

print(pessoa)