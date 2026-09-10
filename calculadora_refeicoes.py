# Criatividade : estou adicionando refrigerantes e sobremesas ao código
# Criatividade: estou calculando refrigerantes e sobremesas ao total geral

# FUNÇÕES DE VALIDAÇÃO COM BLOQUEIO NEGATIVO

def ler_float(mensagem):
    """Garante que o usuário digite um número decimal válido e MAIOR OU IGUAL A ZERO"""
    while True:
        try:
            entrada = input(mensagem).replace(",", ".")
            valor = float(entrada)
            if valor < 0:
                print("❌ Erro: O valor não pode ser negativo! Digite 0 ou um valor maior.")
                continue
            return valor
        except ValueError:
            print("❌ Erro: Digite um preço válido usando apenas números e pontos/vírgulas.")

def ler_int(mensagem):
    """Garante que o usuário digite um número inteiro válido e MAIOR OU IGUAL A ZERO"""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("❌ Erro: A quantidade não pode ser negativa! Digite 0 ou um valor maior.")
                continue
            return valor
        except ValueError:
            print("❌ Erro: Quantidade inválida! Digite apenas números inteiros (ex: 2, 5, 10).")

# CÓDIGO PRINCIPAL

preco_crianca = ler_float("Qual é o preco da refeicao de uma criança?: R$ ") 
preco_adulto = ler_float("Qual é o preco da refeicao de um adulto?: R$ ")

numero_crianca = ler_int("Qual é o numero de criancas: ")
numero_adulto = ler_int("Qual é o numero de adultos: ")

preco_refrigerante = ler_float("Qual é o preco do refrigerante?: R$ ")
numero_refrigerante_vendido = ler_int("Quantos refrigerantes foram vendidos: ")

preco_sobremesa = ler_float("Qual é o preço da sobremesa?: R$ ")
numero_sobremesa_vendida = ler_int("Quantas sobremesas foram vendidas?: ")

total_crianca = preco_crianca * numero_crianca
print(f"\nSubtotal das criancas: R$ {total_crianca:,.2f} ")

total_adulto = preco_adulto * numero_adulto 
print(f"\nSubtotal dos adultos: R$ {total_adulto:,.2f} ")

total_sobremesas = preco_sobremesa * numero_sobremesa_vendida
print(f"\nSubtotal das sobremesas: R$ {total_sobremesas:,.2f} ")

total_refrigerantes = preco_refrigerante * numero_refrigerante_vendido
print(f"\nSubtotal dos refrigerantes R$ {total_refrigerantes:,.2f} ")

subtotal_geral = total_crianca + total_adulto + total_sobremesas + total_refrigerantes
print(f"\nSubtotal Geral: R$ {subtotal_geral:,.2f}")

taxa_imposto = ler_float("Qual é a taxa do imposto sobre as vendas?:(%)  ")
imposto = subtotal_geral * (taxa_imposto / 100)
print(f"\nimposto : R$ {imposto:,.2f} ")

total_geral = subtotal_geral + imposto
print(f"\ntotal_geral : R$ {total_geral:,.2f} ")

pagamento = ler_float("\nQual o valor do pagamento?: R$ ")
troco = pagamento - total_geral
print(f"\ntroco : R$ {troco:,.2f} ")

