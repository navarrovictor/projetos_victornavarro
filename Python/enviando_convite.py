#solicitando os dados do aluno

email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = input("Informe a nota semestral do aluno: ")

#convertendo a note para o formato float

nota_semestral = float(nota_semestral)

#realizando o teste lógico

if nota_semestral > 8.5:
    print("Enviando e-mail para {}".format(email_aluno))

    

