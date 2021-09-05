idade = int(input('Digite a sua idade: '))

if idade <= 14:
    print('Não faz parte da tabela')
else:
    if idade <= 20:
        print('Geração Z')
    elif idade <= 34:
        print('Geração Y')
    elif idade <= 49:
        print('Geração X')
    elif idade < 65:
        print('Geração Baby Boomers')
    else:
        print('Geração Silenciosa')
