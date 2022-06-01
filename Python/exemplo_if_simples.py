rm = input("Insira seu RM: ")
idade = input("Insira sua idade: ")
if int(idade) >= 18:
    print("Sua particiação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações serão enviadas em seu e-mail cadastrado")
else:
    autorizado = input("Você possui autorização dos responsáveis? S-SIM ou N-NÃO ")
    if autorizado == "S":
        print("Sua participação foi autorizada, aluno de RM {}".format(rm))
        print("Mais informações são enviadas para o email dos responsáveis")
    else:
        print("Sua participação não foi autorizada por causa da sua idade")

