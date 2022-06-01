#algoritmo que recebo o VALOR BRUTP do pacote, a
# CATEGORIA DOS ASSENTOS no voo e QUANTIDADE DE VIAJANTES

bruto = float(input("Favor informar o valor bruto: "))
categoria = str(input("Favor informar a categoria Economica, Executiva ou Primeira Classe: "))
qtd_viajantes = int(input("Favor informar a quantidade de viajantes: "))

if categoria == economica:
    if qtd_viajantes == 2:
        print("Os valores são os seguintes: Bruto ", bruto, "Desconto de 3% e ", bruto/qtd_viajante)







