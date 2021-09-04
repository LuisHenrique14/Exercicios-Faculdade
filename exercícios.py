"""idade = int(input('Digite a idade: '))
sexo = input('Escolha o sexo\n[M/m] - Masculino\n[F/f] - Feminino\n')


if ((sexo == 'm') or (sexo == 'M' )):
    if (idade >= 18):
        print(f'É homem e maior de idade')
    else:
        print(f'É homem e menor de idade')
elif ((sexo == 'f') or (sexo == 'F')):
    if (idade >= 21):
        print('É mulher e maior de idade')
    else:
        print('É mulher e menor de idade')
else:
    print(f'Digitou alguma coisa errada')
"""

#APROVADO OU REPROVADO
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 3:
    print(f'O aluno está REPROVADO')
elif (7 > media) and (media >= 3):
    print(f'O aluno está em PROVA FINAL')
    mediaF = float(input('Digite a nota da prova final: '))
    mediaFinal = (mediaF + media) / 2
    if mediaFinal < 5:
        print(f'O aluno está REPROVADO')
    else:
        print(f'O aluno está APROVADO')

else:
    print(f'O aluno está APROVADO')
'''

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,101,1)  #cria um array que vai de 1 a 100
#print(x)
y = np.zeros
#print(y)

y = np.random.normal(5, 1.2, 100)

print(plt.plot(x, y))








