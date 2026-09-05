import time

class Caluculator:
  def __init__(self):
    self.__history = []

  def add(self , *args):
    total = 0
    t = time.time()
    for i in args:
      total = total + i
    self.__history.append({f"Add {t}" : {str(args) : total}})
    return total

  def get_history(self):
    return self.__history;