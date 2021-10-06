import config
run = True

aluno = []
soma = 0

while run:
    command = input("command >> ")

    if command == "exit":
        run = False

    if command == "novo aluno":
        nome = input("Nome: ")
        qtde_notas = int(input("Quantidade de notas: "))
        i = 1

        while i <= qtde_notas:
            nota = float(input(f'Nota {i}: '))

            if nota > config.nota_minina and nota <= config.nota_maxima:
                soma = soma + nota
                i += 1

            else:
                print("Erro! Nota inválida")

        media = soma / qtde_notas
        aluno.append([nome, media])
        relacao = dict(aluno)
        print(relacao)

        if media < config.media_global:
            print(nome + " " + "Reprovado")

        elif media >= config.media_global:
            print("nome" + " " + "Aprovado")

    if command == "exibir":
        if aluno == []:
            print("Relação alunos Vazia")
        else:
            print(relacao)
