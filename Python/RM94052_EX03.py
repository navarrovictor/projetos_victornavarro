#calcula e exibe a media das metades da sala e informa qual metade teve maior nota


total_impar = 0
for x in range(1,50,2):
    impar = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    total_impar = total_impar + impar

total_par = 0
for y in range (2, 51, 2):
    par = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(y)))
    total_par = total_par + par

media_impar = total_impar / 25

media_par = total_par / 25

print("A média do pessoal ímpar foi de: ", media_impar)
print("A média do pessoal par foi de: ", media_par)

if media_impar > media_par:
    print("A maior média foi do pessoal ímpar;")
else:
    print("A maior média foi do pessoal par;")



