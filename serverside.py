import socket,item,main,json,time,os

MAX_BUFFER_SIZE = 4098
server_socket = socket.socket()
selected_items=[]
cut_selected_items = []
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('172.20.10.8',12345))
a = item.getItemJson(main.current_path)
a = json.dumps(a)
server_socket.listen(2)
conn , addr = server_socket.accept()
while True:
    answer_in_bites = conn.recv(MAX_BUFFER_SIZE)
    answer = answer_in_bites.decode('utf_8')
    if str.startswith(answer,'get:'):
        main.current_path = answer[4:]
        print(main.current_path)
        item_dict = item.getItemJson(main.current_path)
        item_dict_bytes = json.dumps(item_dict).encode('utf_8')
        conn.sendall(item_dict_bytes)
    elif str.startswith(answer,'copy:'):
        selected_names = answer[5:]
        selected_items = []
        for i in selected_names.split(',&*^'):
            selected_items.append(item.Item(main.current_path , i, time.ctime(os.path.getmtime(main.current_path + '/' +i)), os.path.getsize(main.current_path + '/' + i)))
    elif str.startswith(answer,'delete:'):
        list = []
        selected_names = answer[7:]
        for i in selected_names.split(',&*^'):
            list.append(item.Item(main.current_path , i, time.ctime(os.path.getmtime(main.current_path + '/' +i)), os.path.getsize(main.current_path + '/' + i)))
        for i in list:
            i.delete() 
        item_dict = item.getItemJson(main.current_path)
        item_dict_bytes = json.dumps(item_dict).encode('utf_8')
        conn.sendall(item_dict_bytes)   
    elif str.startswith(answer,'paste'):
        for i in selected_items:
            i.copy(main.current_path)
        if cut_selected_items and main.current_path != cut_selected_items[0].path:
            for i in cut_selected_items:
                i.copy(main.current_path)
                i.delete()
        item_dict = item.getItemJson(main.current_path)
        item_dict_bytes = json.dumps(item_dict).encode('utf_8')
        conn.sendall(item_dict_bytes)
    elif str.startswith(answer,'cut:'):
        selected_names = answer[4:]
        cut_selected_items = []
        for i in selected_names.split(',&*^'):
            cut_selected_items.append(item.Item(main.current_path , i, time.ctime(os.path.getmtime(main.current_path + '/' +i)), os.path.getsize(main.current_path + '/' + i)))
        item_dict = item.getItemJson(main.current_path)
        item_dict_bytes = json.dumps(item_dict).encode('utf_8')
        conn.sendall(item_dict_bytes)

