#esse programa recebe a distancia e o tempo e calcula a velocida
#primeiro vamos pedir a distancia e o tempo

print("Essa é a calculadora de velocida média")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")

#realizando o cálculo
velocidade_media = float(distancia) / float(tempo)

#exibindo a mensagem
print("A velocidade média calculada foi de {:.2f} km/h".format(velocidade_media))

