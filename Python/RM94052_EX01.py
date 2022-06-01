#algoritmo que recebe o tipo de assinatura do cliente, faturamento anual e calcula o valor do bônus que o cliente deve pagar

tipo_assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ")
faturamento_anual = float(input("Digite o faturamento anual: "))

if tipo_assinatura.upper() == "BASIC":
    bonus = faturamento_anual * 0.3
    print("O valor do bônus a ser pago é de R$", bonus)

if tipo_assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.2
    print("O valor do bônus a ser pago é de R$", bonus)

if tipo_assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.1
    print("O valor do bônus a ser pago é de R$", bonus)

if tipo_assinatura.upper() == "PLATINUM":
    bonus = faturamento_anual * 0.05
    print("O valor do bônus a ser pago é de R$", bonus)

else:
    print("Informe um nome ou valor válido.")




