#programa para informar melhor dia da semana para lives

segunda = int(input("Informe a quantidade de votos que segunda-feira recebeu: "))
terca = int(input("Informe a quantidade de votos que a terça-feira recebeu: "))
quarta = int(input("Informe a quantidade de votos que a quarta-feira recebeu: "))
quinta = int(input("Informe a quantidade de votos que a quinta-feira recebeu: "))
sexta = int(input("Informe a quantidade de votos que a sexta-feira recebeu: "))


if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia da semana escolhido foi segunda-feira.")

if terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia da semana escolhido foi terça-feira.")

if quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print ("O dia da semana escolhido foi quarta-feira.")

if quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print ("O dia da semana escolhido foi quinta-feira.")

if sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print ("O dia da semana escolhido foi sexta-feira.")

else:
    print("Empatou, favor refazer a votação.")