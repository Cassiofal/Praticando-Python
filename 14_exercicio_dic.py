# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1', '3', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opcoes': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opcoes': ['4', '5', '2', '1'],
        'resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta', pergunta['pergunta'])
    print()

    opcoes = pergunta['opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    resposta = input('Escolha uma opção: ')

    print()
    
    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['resposta']:
                acertou = True
        print()
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')
    print()

    print('Você acertou', qtd_acertos)
    print('de', len(perguntas), 'perguntas.')
