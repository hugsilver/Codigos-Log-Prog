produto = "Arroz"
preco_unitario = 5.79
quantidade = 3

# Cálculo do valor total
valor_total = preco_unitario * quantidade

# Aplicando desconto de 10% se a quantidade for maior que 2
if quantidade > 2:
    valor_total = valor_total * 0.8

print("Produto:", produto)
print("Quantidade comprada:", quantidade)
print(f"Valor total da compra: R${valor_total:.2f}")