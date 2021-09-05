senha = int(input('Digite uma senha numerica: '))
d1 = senha // 1000
d2 = senha % 1000 // 100
d3 = senha % 1000 % 100 // 10
d4 = senha % 10

if senha >= 10000 or senha < 1000:
    print(f'SENHA INVÁLIDA')
else:
    if (senha % 2 != 0) and (senha % 17 != 0):
            print(f'Senha FORTE')
    else:
        print(f'Senha FRACA')