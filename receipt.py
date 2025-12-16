from tabulate import tabulate
from datetime import datetime
import os
import utilities as ults
import ast

FILE_RECEIPT = "data/receipts.txt"

def write_receipt(id_client, id_seller, cart, client_name):

  os.makedirs(os.path.dirname(FILE_RECEIPT), exist_ok=True)

  higher_id = 0

  if os.path.exists(FILE_RECEIPT):
    with open(FILE_RECEIPT, "r", encoding="utf-8") as arq:
      for line in arq:
        parts = line.strip().split(";")

        if parts and parts[0].isdigit():
          id_seen = int(parts[0])
          
          if id_seen > higher_id:
            higher_id = id_seen

  new_id = higher_id + 1

  table_data = []
  total_geral = 0.0

  for item in cart:
    cod, name, price, qtd, subtotal = item

    subtotal_float = float(subtotal.replace("R$", "").replace(".", "").replace(",", "."))

    total_geral += subtotal_float
    table_data.append([qtd, name, price, subtotal])

  data = datetime.now().strftime("%d/%m/%Y")

  tax = f"R${(total_geral * 0.25):.2f}".replace(".", ",")
  commission = f"R${(total_geral * 0.05):.2f}".replace(".", ",")

  with open(FILE_RECEIPT, "a", encoding="utf-8") as arq:
    arq.write(f"{new_id};{id_client};{id_seller};{cart};{data};{commission};{tax}\n")

  total_cost = f"R${total_geral:,.2f}"
  total_cost = total_cost.replace(",", "X").replace(".", ",").replace("X", ".")

  table_data.append(["", "", "", ""])
  table_data.append(["", "", "Imposto", tax])
  table_data.append(["", "", "TOTAL", total_cost])
  ults.clean_screen()

  print(f"\nCliente {client_name} comprou no caixa {id_seller}\n")
  header = ["Qtd", "Nome", "Preço", "Subtotal"]

  print(tabulate(
    table_data, headers=header, tablefmt="fancy_grid", stralign="center"
  ))
  print(data)

  ults.confirm()
  

def show_user_purchases(id_client):
  try:
    with open(FILE_RECEIPT, "r", encoding="utf-8") as arq:
      lines = arq.readlines()

    clients_registers = []

    for line in lines:
      parts = line.strip().split(";")

      if len(parts) < 7:
        continue

      id_compra = parts[0]
      id_user = parts[1]
      id_vendedor = parts[2]
      produtos_str = parts[3]
      data = parts[4]
      comissao = parts[5]
      imposto = parts[6]

      if id_user == id_client:
        clients_registers.append({
          "id_compra": id_compra,
          "id_vendedor": id_vendedor,
          "produtos": ast.literal_eval(produtos_str),
          "data": data,
          "comissao": comissao,
          "imposto": imposto
        })

    if not clients_registers:
      print("Nenhuma compra sua foi encontrada.")
      return
    ults.clean_screen()
    for registro in clients_registers:
      print(f"Recibo da compra: #{registro['id_compra']}  |  Cliente: {id_client}  |  Vendedor: {registro['id_vendedor']}")

      tabela = []
      total = 0.0

      for item in registro["produtos"]:
        codigo, nome, preco, qtd, subtotal = item
        tabela.append([qtd, nome, preco, subtotal])

        sub_clean = subtotal.replace("R$", "").replace(".", "").replace(",", ".")
        total += float(sub_clean)

      headers = ["Qtd", "Nome", "Preço", "Subtotal"]
      
      tabela.append(["", "", "", ""])
      tabela.append(["", "", "Imposto", registro["imposto"]])
      

      total_fmt = f"R${total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

      tabela.append(["", "", "TOTAL", total_fmt])
      print(tabulate(tabela, headers=headers, tablefmt="fancy_grid"))

      print(registro["data"])
      ults.separate()

  except FileNotFoundError:
    print("Arquivo de relatórios não encontrado.")


def report_between_dates(data_initial, data_end):
  try:
    with open(FILE_RECEIPT, "r", encoding="utf-8") as arq:
      lines = arq.readlines()

    d1 = datetime.strptime(data_initial, "%d/%m/%Y")
    d2 = datetime.strptime(data_end, "%d/%m/%Y")

    if d1 > d2:
      d1, d2 = d2, d1

    products_sold = {}
    total_sold = 0.0
    total_tax = 0.0
    commission_4_seller = {}

    datas_founds = set()

    for line in lines:
      parts = line.strip().split(";")
      if len(parts) < 7:
        continue

      id_compra = parts[0]
      id_cliente = parts[1]
      id_vendedor = parts[2]
      produtos_str = parts[3]
      data = parts[4]
      comissao = parts[5]
      imposto = parts[6]

      datas_founds.add(data)

      d_compra = datetime.strptime(data, "%d/%m/%Y")

      if not (d1 <= d_compra <= d2):
        continue

      imposto_float = float(imposto.replace("R$", "").replace(".", "").replace(",", "."))
      total_tax += imposto_float

      com_float = float(comissao.replace("R$", "").replace(".", "").replace(",", "."))
      commission_4_seller[id_vendedor] = commission_4_seller.get(id_vendedor, 0) + com_float

      produtos = ast.literal_eval(produtos_str)
      for item in produtos:
        codigo, nome, preco, qtd, subtotal = item

        qtd = int(qtd)

        sub_clean = subtotal.replace("R$", "").replace(".", "").replace(",", ".")
        total_sold += float(sub_clean)

        if codigo not in products_sold:
          products_sold[codigo] = {"nome": nome, "qtd": 0}

        products_sold[codigo]["qtd"] += qtd

      ults.clean_screen()
      print("Datas de compra disponíveis")
      for dt in sorted(datas_founds, key=lambda x: datetime.strptime(x, "%d/%m/%Y")):
        print("-", dt)
      ults.separate()
      print("Relatorio do período")
      print(f"Período: {data_initial} até {data_end}")
      ults.separate()

      tabela_produtos = [
        [codigo, info["nome"], info["qtd"]]
        for codigo, info in products_sold.items()
      ]

      if tabela_produtos:
        print("Podutos vendidos:")
        print(tabulate(tabela_produtos, headers=["Código", "Nome", "Quantidade"], tablefmt="fancy_grid"))
      else:
        print("Nenhuma venda nesse período.")

      total_sold_fmt = f"R${total_sold:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
      total_tax_fmt = f"R${total_tax:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
      ults.separate()
      print("Total de vendas:", total_sold_fmt)
      print("Total de imposto:", total_tax_fmt)

      print("Comissão por vendedor:")
      tabela_com = [
        [vendedor, f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")]
        for vendedor, valor in commission_4_seller.items()
      ]
      print(tabulate(tabela_com, headers=["Vendedor", "Comissão"], tablefmt="fancy_grid"))
      ults.separate()
    ults.confirm()

  except FileNotFoundError:
    print("Arquivo de relatórios não encontrado.")