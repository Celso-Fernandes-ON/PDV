FILE_PRODUCTS = "data/products.txt"

import os
from time import sleep

def separate():
  print("\033[32m-=-"*20,"\33[m")


def clean_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  separate()


def confirm():
  input("Aperte Enter para continuar...")


def load(msg):
  for i in range(4):
    print(f"\r{msg}{'.' * i}", end="", flush=True)
    sleep(0.3)
  print(f"\r{msg}... \033[34mpronto!\033[m")
  sleep(0.5)


def error(msg):
  print(f"\033[31mERROR: {msg}\33[m")
  confirm()


def file_write(file, id_num, name):
  with open(file, "a", encoding="utf-8") as arq:
    arq.write(f"{id_num};{name}\n")