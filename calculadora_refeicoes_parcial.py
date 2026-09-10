# O preço da refeição de uma criança (ponto flutuante)
preco_crianca = float(input("Qual é o preco da refeicao de uma criança?: R$ ")) 
# O preço da refeição de um adulto (ponto flutuante)
preco_adulto = float(input("Qual é o preco da refeicao de um adulto?: R$ "))
# O número de crianças (inteiro)
numero_crianca = int(input("Qual é o numero de criancas: "))
# O número de adultos (inteiro)
numero_adulto = int(input("Qual é o numero de adultos: "))
# Calculando os totais relativos às crianças e adultos
total_crianca = preco_crianca * numero_crianca
total_adulto = preco_adulto * numero_adulto 
# Calculando o subtotal apenas das refeições
subtotal = total_crianca + total_adulto
# Exibindo o valor total 
print(f"\nSubtotal: R$ {subtotal:,.2f} ")