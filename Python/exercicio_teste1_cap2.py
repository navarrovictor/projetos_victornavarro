batimentos = int(input("Informe o seu número de BATIMENTOS POR MINUTO (BPM): "))
idade = int(input("Informe a sua idade: "))

if idade <= 2 and 120 <= batimentos <= 140 or 8 <= idade <= 17 and 80 <= batimentos <= 100 or 18 <= idade <= 60 and 70 <= batimentos <= 80:
    print("Dentro da faixa adequada.")

else:
    print("Fora da faixa adequada.")

