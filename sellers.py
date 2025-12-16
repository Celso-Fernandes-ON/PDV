FILE_SELLER = "data/sellers.txt"

import os
import verifies
import utilities as ults
from tabulate import tabulate


def seller_list():
  try:
    if not os.path.exists(FILE_SELLER):
      print("Nenhum vendedor cadastrado ainda.")
      return

    print("\nVendedores cadastrados:")

    seller = []
    with open(FILE_SELLER, "r", encoding="utf-8") as arq:
      for line in arq:
        seller.append(line.strip().split(";"))

    if not seller:
      ults.clean_screen()
      print("O arquivo está vazio.")
      return

    header = ["Número do vendedor", "Nome do vendedor"]
    print(tabulate(seller, headers=header, tablefmt="fancy_grid"))
    
    return seller

  except FileNotFoundError:
    print("Nenhum vendedor cadastrado ainda.")

def seller_register():
  os.makedirs(os.path.dirname(FILE_SELLER), exist_ok=True)
  name = input("Nome do vendedor: ")
  
  if name:
    id_seller = verifies.get_next_sequential_id()
    ults.file_write(FILE_SELLER, id_seller, name)

    ults.clean_screen()
    seller = [id_seller, name]
    header = ["Número do vendedor", "Nome do vendedor"]

    print("Vendedor cadastrado com sucesso!")
    print(tabulate([seller], headers=header, tablefmt="fancy_grid"))

    ults.confirm()
    ults.clean_screen()

  else:
    print("Preencha o campo do nome")
    ults.separate()
    seller_register()


def seller_delete():
  if not os.path.exists(FILE_SELLER):
    print("Nenhum vendedor cadastrado ainda.")
    return False
  
  seller_list()
  ults.separate()
  print("Identificação do vendedor:")

  id_seller = input()
  ults.clean_screen()

  new_lines = []
  removed = False
  with open(FILE_SELLER, "r", encoding="utf-8") as arq:
    for lines in arq:
      parts = lines.strip().split(";")
      if parts[0] == id_seller:
        removed = True, parts[1]
        continue 
      new_lines.append(lines)

  if not removed:
    print(f"ID {id_seller} não encontrado.")
    return False

  with open(FILE_SELLER, "w", encoding="utf-8") as arq:
    arq.writelines(new_lines)

  print(f"\033[33mVendedor {removed[1]} com ID {id_seller} removido com sucesso.\33[m")
  return True