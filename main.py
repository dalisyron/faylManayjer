import terminal_ui
import item
import os
import time

current_path = '/'
file_list = item.getItemList(current_path)

def getPath(current_path, new_directory):
  if (current_path == '/'):
    return '/' + new_directory
  else:
    return current_path + '/' + new_directory