FILE_CLIENTS = "data/clients.txt"

import os
import verifies
import utilities as ults
from tabulate import tabulate

def register_client():
  os.makedirs(os.path.dirname(FILE_CLIENTS), exist_ok=True)
  name = input("Insira seu nome: ")
  if name:

    new_id = verifies.single_id("CL",FILE_CLIENTS)
    
    ults.file_write(FILE_CLIENTS, new_id, name)
    
    clint = [[new_id, name]]
    header = ["ID","Nome"]

    print(tabulate(clint, headers=header, tablefmt="fancy_grid"))
    
    return new_id
  else:
    print("Preencha o campo do nome")
    ults.separate()
    register_client()
