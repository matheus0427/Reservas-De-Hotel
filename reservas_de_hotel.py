
cliente1_nome = input("Digite o nome do Cliente 1: ")
cliente1_idade = int(input("Digite a idade do Cliente 1: "))
cliente2_nome = input("Digite o nome do Cliente 2: ")
cliente2_idade = int(input("Digite a idade do Cliente 2: "))
cliente3_nome = input("Digite o nome do Cliente 3: ")
cliente3_idade = int(input("Digite a idade do Cliente 3: "))
print("\nEscolha o tipo de quarto para cada cliente:")
print("1 - Simples (R$ 100,00 por dia)")
print("2 - Duplo (R$ 150,00 por dia)")
print("3 - Luxo (R$ 250,00 por dia)")
cliente1_quarto = int(input(f"Escolha o quarto para {cliente1_nome}: "))
cliente1_dias = int(input(f"Quantos dias {cliente1_nome} ficará no hotel? "))
cliente2_quarto = int(input(f"Escolha o quarto para {cliente2_nome}: "))
cliente2_dias = int(input(f"Quantos dias {cliente2_nome} ficará no hotel? "))
cliente3_quarto = int(input(f"Escolha o quarto para {cliente3_nome}: "))
cliente3_dias = int(input(f"Quantos dias {cliente3_nome} ficará no hotel? "))
preco_simples = 100
preco_duplo = 150
preco_luxo = 250
if cliente1_quarto == 1:
    valor_cliente1 = preco_simples * cliente1_dias
elif cliente1_quarto == 2:
    valor_cliente1 = preco_duplo * cliente1_dias
elif cliente1_quarto == 3:
    valor_cliente1 = preco_luxo * cliente1_dias
else:
    valor_cliente1 = 0
    print("Tipo de quarto inválido para o Cliente 1.")
if cliente2_quarto == 1:
    valor_cliente2 = preco_simples * cliente2_dias
elif cliente2_quarto == 2:
    valor_cliente2 = preco_duplo * cliente2_dias
elif cliente2_quarto == 3:
    valor_cliente2 = preco_luxo * cliente2_dias
else:
    valor_cliente2 = 0
    print("Tipo de quarto inválido para o Cliente 2.")
if cliente3_quarto == 1:
    valor_cliente3 = preco_simples * cliente3_dias
elif cliente3_quarto == 2:
    valor_cliente3 = preco_duplo * cliente3_dias
elif cliente3_quarto == 3:
    valor_cliente3 = preco_luxo * cliente3_dias
else:
    valor_cliente3 = 0
    print("Tipo de quarto inválido para o Cliente 3.")
print("\nResumo das Reservas:")
print(f"{cliente1_nome} deve pagar R$ {valor_cliente1:.2f}.")
print(f"{cliente2_nome} deve pagar R$ {valor_cliente2:.2f}.")
print(f"{cliente3_nome} deve pagar R$ {valor_cliente3:.2f}.")