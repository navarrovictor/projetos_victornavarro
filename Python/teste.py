#importação do módulo calc.py

from calc import *
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

#armazenando a soma
soma = somar(valor1, valor2)

#exibindo a soma
print("A soma é {}".format(soma))

subtrai = subtrair(valor1, valor2)
print("A subtração é {}".format(subtrai))

