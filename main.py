import terminal_ui
import item
import os
import time

current_path = '/Users/hamidreza/Desktop'
file_list = item.getItemList(current_path)
terminal_ui.printItemList(file_list)