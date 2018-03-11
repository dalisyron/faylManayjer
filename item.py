import time
import os

class Item:
  def __init__(self, path, name, date, par_item = None):
    self.path = path
    self.name = name
    self.date = date
    self.par_item = par_item

def getItemList(path):
  str_file_list = os.listdir(path)
  result = []
  for i in str_file_list:
    tmp_item = Item(path, i, time.ctime(os.path.getmtime(path + '/' + i)))
    result.append(tmp_item)
  return result