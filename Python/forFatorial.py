numero = int(input("Digite o número inteiro para calcular o fatorial: "))


fatorial = 1
for i in range(1, numero + 1):
    fatorial = fatorial * i

print("Fatorial de " + str(numero) + " é: " + str(fatorial))