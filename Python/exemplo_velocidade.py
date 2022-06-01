def calcularVelocidadeMedia():
    distancia = float(input("Digite a distancia percorrida: "))
    tempo = float(input("Digite o tempo da viagem: "))

    velocidade_media = distancia/tempo

    print("A velocidade média é {} km/h".format(velocidade_media))

calcularVelocidadeMedia()