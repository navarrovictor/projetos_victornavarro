arquivo = open("C:\\Users\\victo\\OneDrive\\Área de Trabalho\\arquivo_de_texto.txt")



#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)
arquivo.close()