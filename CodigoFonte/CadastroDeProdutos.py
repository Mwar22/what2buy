listaCompras = []
print("Lista de Compras")
while True:
     produto = input("Digite o nome do Produto ou '0' para terminar: ")
     if produto == '0':
         break
     quantidade = int(input("Quantidade: "))
     preco = float(input("Preço: "))
     listaCompras.append([produto, quantidade, preco])
soma = 0.0
for e in listaCompras:
     print("%20s: %5d x %5.2f =%6.2f" % (e[0],
                         e[1],e[2],
                         e[1] * e[2]))
     soma += e[1] * e[2]
print("Total R$: %7.2f" % soma)
