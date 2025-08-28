estoque={   "caderno": [ 1000, 2.30],
            "lapis": [ 500, 0.45],
			"caneta": [ 2001, 1.20],
			"marcador": [ 100, 1.50],
            "fichario": [100, 3.50],
            "papel sulfite": [200, 2.30],
            "cola bastão": [50, 1.30],
            "fita": [300, 2.50],
            "cola liquida": [100, 0.40],
            "pasta": [900, 4.30],
            "mochila": [1180, 2.30],
            "estojo": [1000, 2.30],
            "borracha": [900, 2.90],
            "apontador": [900, 4.50],
            "estilete": [200, 6.30],
            "tesoura": [200, 2.30],
            "papel canson": [200, 2.30],
            "impressora": [200, 2.30],
            "cartolina colorida": [2000, 2.30],
            "tinta guache": [1000, 2.30] }

slk_pae = input("digite o produto:")
venda = [ [slk_pae, int(input("digite a quantidade:"))] ]
total = 0
print("Vendas:\n")
if slk_pae in estoque:
    for operação in venda:
      produto, quantidade = operação 
      preço = estoque[produto][1] 
      custo = preço * quantidade
      print("%12s: %3d x %6.2f = %6.2f" %
	  (produto, quantidade,preço,custo))
      estoque[produto][0] -= quantidade 
      total+=custo
else:
    print("insuficiente!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])