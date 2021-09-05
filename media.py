n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
try:
    if media < 3:
        print(f'O aluno está REPROVADO')
    else:
        if media < 7:
            print(f'O aluno ficou em PROVA FINAL')
            mediaF = float(input('Digite a nota da prova final: '))
            mediaFinal = (mediaF + media) / 2
            if mediaFinal < 5:
                print(f'O aluno está REPROVADO')
            else:
                print(f'O aluno está APROVADO')
        else:
            print(f'O aluno está APROVADO')
except Exception as erro:
    print(f'Erro {erro}')

