#programa que recebe os minutos atuais e exibe na tela a senha necessária para desbloqueio, usando fatorial

minutos = int(input("Digite os minutos atuais: "))

if minutos <= 60:
    fatorial = 1
    for i in range(1, minutos + 1, 1):
        fatorial = fatorial * i
    print("A senha de acordo com os minutos é LIBERDADE{}".format(fatorial))

else:
    print("Digite um valor de minutos válido.")


