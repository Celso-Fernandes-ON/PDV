FILE_PRODUCTS = "data/products.txt"


import os
import verifies
import sellers
import receipt
import utilities as ults
from tabulate import tabulate


def products_register():
  os.makedirs(os.path.dirname(FILE_PRODUCTS), exist_ok=True)
  while True:
    print("Cadastro de Produto")

    name = input("Nome do produto: ").strip().capitalize()
    valor_str = input("Valor do produto (ex: 12.99 ou R$12,99): ").strip()
    stock_str = input("Estoque inicial: ").strip()
    ults.separate()

    if not name or not valor_str or not stock_str:
      ults.error("Nenhum campo pode ficar vazio. Tente novamente.")
      ults.clean_screen()
      return

    try:
      valor_clean = valor_str.replace("R$", "").replace("r$", "").replace(",", ".").strip()
      
      valor = float(valor_clean)
    except ValueError:
      ults.error("Valor inválido! Use números (ex: 12.99).")
      continue

    try:
      stock = int(stock_str)
      if stock < 0:
        raise ValueError
    except ValueError:
      ults.error("Estoque deve ser um número inteiro positivo.")
      continue

    break
  new_id = verifies.single_id("PR",  FILE_PRODUCTS)

  with open(FILE_PRODUCTS, "a", encoding="utf-8") as arq:
    arq.write(f"{new_id};{name};{valor};{stock}\n")

  print("Produto cadastrado com sucesso!")


def products_list():

  try:
    print("Produtos cadastrados:")
    products = []
    products_with_id = []

    with open(FILE_PRODUCTS, "r", encoding="utf-8") as arq:

      for index, lines in enumerate(arq, start=1):
        id_code, name, price, stock = lines.strip().split(";")
        
        price_float = float(price)
        preco_formatado = f"R${price_float:,.2f}".replace(",", "X").replace(".", ",").replace("X",".")

        products.append([index, name, preco_formatado, stock])
        products_with_id.append([id_code, index, name, preco_formatado, stock])

      if not products:
        ults.clean_screen()
        print("O arquivo está vazio.")
        return products_with_id
      
      
    header = ["Codigo", "Nome ", "preço", "Estoque"]
    print(tabulate(products, headers=header, tablefmt="fancy_grid"))
    return products_with_id
      
  except FileNotFoundError:
    print("Nenhum produto cadastrado ainda.")


def product_delete():
  products_list()
  print("ID do produto para remover: ")
  ults.separate()
  id_input = (input())

  if id_input.isdigit():
    id_remove = int(id_input)
    ults.separate()

    try:

      with open(FILE_PRODUCTS, "r", encoding="utf-8") as arq:
        lines = arq.readlines()

      index_remover = id_remove - 1

      if index_remover < 0 or index_remover >= len(lines):
        ults.error("ID não encontrado!")
        return False

      produto_removido = lines[index_remover].strip().split(";")
      print(f"Produto removido: {produto_removido[1]} (Preço {produto_removido[2]})")

      with open(FILE_PRODUCTS, "w", encoding="utf-8") as arq:
        for i, linha in enumerate(lines):
          if i != index_remover:
            arq.write(linha)

      print("Removido com sucesso.")
      return True

    except FileNotFoundError:
      ults.error("O arquivo de produtos não existe.")
      return False
  else:
    ults.error("Número deve ser inteiro")


def product_update(index_product, amount):
  list_products = []

  try:
    with open(FILE_PRODUCTS, "r", encoding="utf-8") as arq:
      for line in arq:
        list_products.append(line.strip().split(";"))

    if index_product < 0 or index_product >= len(list_products):
        ults.error("Índice do produto inválido.")
        return False
    
    code, name, price, stock = list_products[index_product]

    new_stock = int(stock) + amount
    if new_stock < 0:
      ults.error(f"Estoque insuficiente (estoque atual: {stock}).")
      return False

    list_products[index_product][3] = str(new_stock)

    with open(FILE_PRODUCTS, "w", encoding="utf-8") as arq:
      for product in list_products:
        arq.write(";".join(product) + "\n")

    product_updated = f"Estoque atualizado: {name} agora possui {new_stock} unidades."
    return product_updated

  except FileNotFoundError:
    ults.error("O arquivo de produtos não existe.")
    return False


def products_buy(client):
  products = products_list()
  cart = []

  while True:
  
    if cart:
      print("[cancelar] para cancelar")
      print("[finalizar] para finalizar as compras")

    ults.separate()
    id_input = input("ID do produto para comprar: ").strip().lower()

    if id_input == "cancelar":
      ults.load("Cancelando")
      return None

    if id_input == "finalizar":
      final_cart = []
      seller_free = sellers.seller_list()

      if seller_free:
        while True:
          print("Escolha o caixa para ser atendido")
          ults.separate()
          client_op_seller = input()

          if client_op_seller.isdigit():
            seller_select = int(client_op_seller)

            if 0 < seller_select and seller_select <= len(seller_free):
            
              for prod_id, qtd in cart:
                code, index, name, price, stock = products[prod_id]

                price_float = float(price.replace("R$", "").replace(".","").replace(",", "."))
                total = price_float * qtd
                total_formatado = f"R${total:.2f}".replace(".", ",")
                product_update(prod_id, -qtd)

                final_cart.append([
                  code, name, price, str(qtd), total_formatado
                ])

              receipt.write_receipt(client[0],seller_select,final_cart,client[1])
              return
            else:
              ults.error("ID invalido")
              continue
          
          if not client_op_seller.isdigit():
            ults.error("O ID deve ser um número inteiro.")
            continue
        
      else:
        ults.error("Infelizmente não temos caixa disponível")
      

    if not id_input.isdigit():
      ults.error("O ID deve ser um número inteiro.")
      continue

    id_input = int(id_input) - 1 

    if id_input < 0 or id_input >= len(products):
      ults.error("Esse ID não existe na lista de produtos.")
      continue

    product = products[id_input]
    code, index, name, price, stock = product


    qtd_str = input("Quantidade desejada: ").strip()

    if not qtd_str.isdigit():
      ults.error("A quantidade deve ser um número inteiro.")
      continue

    qtd = int(qtd_str)

    if qtd <= 0:
      ults.error("Quantidade inválida.")
      continue

    if qtd > int(stock):
      ults.error("Quantidade maior que o estoque disponível.")
      continue

    cart.append([id_input, qtd])
    print(f"{name} x{qtd} adicionado ao carrinho!\n")
    
  