import item

def printItemList(item_list):
  mx = 0
  for i in item_list:
    mx = max(mx, len(i.name))
  for i in item_list:
    print('{}{}{}'.format(i.name, ' ' * (mx + 5 - len(i.name)),i.date))