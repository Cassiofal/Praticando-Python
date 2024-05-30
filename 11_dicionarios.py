# Dicioários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chaves" e "valor"
# chaves pedem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de quaquer tipo, incluindo outro
# dicionário.
# Usamos as cahves - {} - ou classe dict para cirar
# dicionários.
# Imutáveis: dict, list



pessoas = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

print(pessoas['nome'])
print()
# Dicionário não é iterável, mas o Python aceita pegar 
# uma variável dentro do dicionário pessaos.
for chave in pessoas:
    print(chave, pessoas[chave])