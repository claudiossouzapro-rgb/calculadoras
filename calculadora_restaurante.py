# Criatividade : estou adicionando refrigerantes e sobremesas ao código
# Criatividade: estou calculando refrigerantes e sobremesas ao total geral

# O preço da refeição de uma criança (ponto flutuante)
preco_crianca = float(input("Qual é o preco da refeicao de uma criança?: R$ ")) 
#  O preço da refeição de um adulto (ponto flutuante)
preco_adulto = float(input("Qual é o preco da refeicao de um adulto?: R$ "))
# O número de crianças (inteiro)
numero_crianca = int(input("Qual é o numero de criancas: "))
# O número de adultos (inteiro)
numero_adulto = int(input("Qual é o numero de adultos: "))
# O preço do refirgerante (ponto flutuante)
preco_refrigerante = float(input("Qual é o preco do refrigerante?: R$ "))
# O número dos refrigerantes vendidos(inteiro)
numero_refrigerante_vendido = int(input("Quantos refrigerantes foram vendidos: "))
# O preço da sobremesa (ponto flutuante)
preco_sobremesa = float(input("Qual é o preço da sobremesa?: R$ "))
# O número de sobremesas vendidas (inteiro)
numero_sobremesa_vendida = int(input("Quantas sobremesas foram vendidas?: "))
# Calculando os totais relativos as crianças (ponto flutuante)
total_crianca = preco_crianca * numero_crianca
print(f"\nSubtotal das criancas: R$ {total_crianca:,.2f} ")
# Calculando os totais relativos aos adultos(ponto flutuante)
total_adulto = preco_adulto * numero_adulto 
print(f"\nSubtotal dos adultos: R$ {total_adulto:,.2f} ")
# Calculando os totais relativos as sobremesas (ponto flutuante)
total_sobremesas = preco_sobremesa * numero_sobremesa_vendida
print(f"\nSubtotal das sobremesas: R$ {total_sobremesas:,.2f} ")
# Calculando os totais relativos aos refrigerantes (ponto flutuante)
total_refrigerantes = preco_refrigerante * numero_refrigerante_vendido
print(f"\nSubtotal dos refrigerantes R$ {total_refrigerantes:,.2f} ")
# Total_Geral
# Calculando o subtotal geral da conta
subtotal_geral = total_crianca + total_adulto + total_sobremesas + total_refrigerantes
# Calculando o subtotal geral da conta
subtotal_geral = total_crianca + total_adulto + total_sobremesas + total_refrigerantes
# Exibindo o valor total formatado COM a vírgula para o milhar e o ponto para os centavos
print(f"\nSubtotal Geral: R$ {subtotal_geral:,.2f}")
# Pedir a taxa do imposto ao usuario (ponto flutuante)
taxa_imposto = float(input("Qual é a taxa do imposto sobre as vendas?:(%)  "))
# Calcular o valor do imposto
imposto = subtotal_geral * (taxa_imposto / 100)
print(f"\nimposto : R$ {imposto:,.2f} ")
# Calcular o total geral
total_geral = subtotal_geral + imposto
print(f"\ntotal_geral : R$ {total_geral:,.2f} ")
# Pedir o valor do pagamento ao usuario (ponto flutuante)
pagamento = float(input("\nQual o valor do pagamento?: R$ ").replace(",", "."))
# Calcular o troco
troco = pagamento - total_geral
print(f"\ntroco : R$ {troco:,.2f} ")

