import products
import verifies
import sellers
import clients
import receipt
import utilities as ults


while True:
  ults.clean_screen()
  print("[1] - Entrar")
  print("[2] - Criar conta")
  ults.separate()
  option = input(": ").strip().lower()

  if(option=="1"):
    ults.clean_screen()
    account = verifies.sign_in()

    if account[0] == "back":
      ults.load("Voltando")

    elif account[0] == "adm":
      ults.load("Carregando")

      ults.clean_screen()

      while True:
        print("Permissão de administrador identificado")
        print("Bem-vindo de volta SR.")

        ults.separate()

        print("[1] - Gerenciar Vendedores")
        print("[2] - Gerenciar  Estoque")
        print("[3] - Ralatório de vendas")
        print("[SAIR] - para volta")

        ults.separate()
        adm_op = input()
        ults.clean_screen()

        if adm_op.lower() == "sair":
          ults.load("Saindo")
          break

        elif(adm_op == "1"):
          sellers.seller_list()

          while True:
            ults.separate()
            print("[1] - Adicionar Vendedores")
            print("[2] - Remover Vendedores")
            print("[VOLTAR] - para volta")

            ults.separate()
            adm_seller_op = input().strip().lower()
            ults.clean_screen()

            if adm_seller_op == "1":
              sellers.seller_register()
            elif adm_seller_op == "2":
              sellers.seller_delete()
              sellers.seller_list()
            elif adm_seller_op == "voltar":
              ults.load("Voltando")
              break
            else:
              ults.error("Selecione uma opção, 1 ou 2")

        elif(adm_op == "2"):
          while True:
            ults.clean_screen()
            print("[1] - Adicionar Produto")
            print("[2] - Remover Produto")
            print("[3] - Atualizar estoque do Produto")
            print("[4] - Listar Produto")
            print("[VOLTAR] - para volta")

            ults.separate()
            adm_stock_op = input().strip().lower()
            ults.clean_screen()

            if adm_stock_op == "1":
              products.products_register()
            elif adm_stock_op == "2":
              products.product_delete()
              ults.confirm()

            elif adm_stock_op == "3":
              list_products = products.products_list()
              ults.separate()
              id_product = input("Id do produto:\n").strip()

              if not id_product.isdigit():
                ults.error("ID deve ser número!")
                continue
              id_product = int(id_product)

              if id_product > len(list_products):
                ults.error("Esse id está errado")
                continue
              amount = input("Quantidade a adicionar:\n").strip()

              if not amount.lstrip("-").isdigit():
                ults.error("Quantidade deve ser número!")
                continue

              amount = int(amount)

              msg = products.product_update(id_product-1, amount)
              print(msg)

            elif adm_stock_op == "4":
              products.products_list()
              ults.confirm()
            elif adm_stock_op == "voltar":
              ults.load("Voltando")
              break
            else:
              ults.error("Selecione uma opção, 1, 2 ou 3")
        elif(adm_op == "3"):
          print("EX: 03/12/2025")
          start_data = input("Data de início:")
          end_data = input("Data de fim:")
          
          if start_data and end_data:
            ults.separate()
            receipt.report_between_dates(start_data, end_data)
        else:
          ults.error("Selecione uma opção, 1, 2 ou 3")
          ults.separate()

    elif account[0] == "client":
      ults.load("Carregando")
      signed = account[1]

      while True:
        ults.clean_screen()
        print(f"Bem-vindo as compras \033[36m{signed[1]}\33[m")
        ults.separate()
        print("[1] - Iniciar as compras")
        print("[2] - Historico de compras")
        print("[SAIR] - Para volta")
        ults.separate()
        client_op = input().strip()
        ults.clean_screen()

        if client_op.lower() == "sair":
          ults.load("Saindo")
          break
        elif client_op == "1":
          ults.load("Carregando produtos")
          products.products_buy(signed)

        elif client_op == "2":
          ults.load("Carregando historico")
          receipt.show_user_purchases(signed[0])
          ults.confirm()
          
        else:
          ults.error("Selecione uma opção, 1 ou 2")


      ults.confirm()

    else:
      ults.error("inesperado ao detectar o tipo de conta")


  elif(option == "2"):
    ults.clean_screen()
    clients.register_client()
    ults.confirm()


  elif(option=="stop"):
    ults.clean_screen()

    ults.load("Finalizando")
    ults.separate()
    break
  else:
    ults.error("Selecione uma opção, 1 ou 2")