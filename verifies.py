FILE_CLIENTS = "data/clients.txt"
FILE_SELLER = "data/sellers.txt"


import os
import random
import string
from time import sleep
import utilities as ults

def sign_in():
  while True:
    print("[VOLTAR] - para volta")
    print("ou Insira seu ID:")
    ults.separate()
    id_entry = input().strip()

    if id_entry.lower() == "voltar":
      return "back",""

    if len(id_entry) == 8:
      id_response = id_exists(id_entry, FILE_CLIENTS)

      if id_response:
        if (id_response[1][0]) == "CL236669":
          return "adm",""
        else:
          return "client", id_response[1]
      return "",""

    ults.clean_screen()
    print("Seu ID deve ter 8 digitos")
    sleep(1)

    ults.clean_screen()
    print("\033[33mTente novamente\33[m")
    sleep(1)

def single_id(initial_id, file):
  while True:
    new_id = initial_id + ''.join(random.choice(string.digits) for _ in range(6))
    if not id_exists(new_id, file):
      break
  return new_id
  

def id_exists(id_sought, file):

  if not os.path.exists(file):
    return False

  with open(file, "r", encoding="utf-8") as arq:
    for lines in arq:
      parts = lines.strip().split(";")
      if parts and parts[0] == id_sought:
        return True, parts
  return False


def get_next_sequential_id():
  ids = []

  if not os.path.exists(FILE_SELLER):
    return "001"

  with open(FILE_SELLER, "r", encoding="utf-8") as arq:
    for lines in arq:
      parts = lines.strip().split(";")
      if parts:
        try:
          ids.append(int(parts[0]))
        except ValueError:
            pass
  if not ids:
    return "001"

  ids.sort()
  expected = 1
  for id_num in ids:
    if id_num != expected:
      break
    expected += 1

  return f"{expected:03d}"