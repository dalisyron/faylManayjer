import time
import os
import shutil
#github usernames added

class Item:
    def __init__(self, path, name, date, size, par_item=None):
        self.path = path
        self.name = name
        self.date = date
        self.size = size
        self.par_item = par_item

    def copy(self, destination):
        if os.path.isdir(self.path + '/' + self.name):
            shutil.copytree(self.path + '/' + self.name, destination + '/' + self.name)
        else:
            shutil.copyfile(self.path + '/' + self.name, destination + '/' + self.name)

    def delete(self):
        if os.path.isdir(self.path + '/' + self.name):
            shutil.rmtree(self.path + '/' + self.name)
        else:
            os.remove(self.path + '/' + self.name)
    def rename(self,new_name):
        os.rename(self.path+'/'+self.name ,self.path+'/'+new_name)
def getItemList(path):
    str_file_list = os.listdir(path)
    result = []
    for i in str_file_list:
        #tmp_item = Item(path, i, time.ctime(os.path.getmtime(path + '/' + i)), os.path.getsize(path + '/' + i))
        slash = '/'
        if (path == '/'):
            slash = ''
        tmp_item = Item(path, i, time.ctime(os.path.getmtime(path + slash + i)), os.path.getsize(path + slash + i))
        result.append(tmp_item)
    return result
