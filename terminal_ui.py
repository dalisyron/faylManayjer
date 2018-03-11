import item

def printItemList(item_list):
  for i in item_list:
    print('{}/{}  {}'.format(i.path, i.name, i.date))
