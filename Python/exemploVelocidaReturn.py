def calcularVelocidadeMedia(distancia, temp):

    velocidade_media = distancia/temp

    return velocidade_media
dist = float(input("Informe a distância: "))
temp = float(input("Informe o tempo: "))

print("A velocidade média é de {}".format(calcularVelocidadeMedia(dist, temp)))