import socket,item,main,json,time,os
from threading import Thread
def client_service(conn, ip, port,clients,MAX_BUFFER_SIZE=4098):
    selected_items = []
    cut_selected_items = []
    while True:
        answer_in_bites = conn.recv(MAX_BUFFER_SIZE)
        answer = answer_in_bites.decode('utf_8')
        if str.startswith(answer, 'get:'):
            main.current_path = answer[4:]
            item_dict = item.getItemJson(main.current_path)
            item_dict_bytes = json.dumps(item_dict).encode('utf_8')
            conn.sendall(item_dict_bytes)
        elif str.startswith(answer, 'copy:'):
            selected_names = answer[5:]
            cut_selected_items = []
            selected_items = []
            for i in selected_names.split(',&*^'):
                selected_items.append(
                    item.Item(main.current_path, i, time.ctime(os.path.getmtime(main.current_path + '/' + i)),
                              os.path.getsize(main.current_path + '/' + i)))
        elif str.startswith(answer, 'delete:'):
            list = []
            selected_names = answer[7:]
            for i in selected_names.split(',&*^'):
                list.append(item.Item(main.current_path, i, time.ctime(os.path.getmtime(main.current_path + '/' + i)),
                                      os.path.getsize(main.current_path + '/' + i)))
            for i in list:
                i.delete()
            item_dict = item.getItemJson(main.current_path)
            item_dict_bytes = json.dumps(item_dict).encode('utf_8')
            conn.sendall(item_dict_bytes)
        elif str.startswith(answer, 'paste'):
            try:
                for i in selected_items:
                    i.copy(main.current_path)
                if cut_selected_items and main.current_path != cut_selected_items[0].path:
                    for i in cut_selected_items:
                        i.copy(main.current_path)
                        i.delete()
            except:
                print("could not paste!!!")
            item_dict = item.getItemJson(main.current_path)
            item_dict_bytes = json.dumps(item_dict).encode('utf_8')
            conn.sendall(item_dict_bytes)
        elif str.startswith(answer, 'cut:'):
            selected_names = answer[4:]
            cut_selected_items = []
            selected_items = []
            for i in selected_names.split(',&*^'):
                cut_selected_items.append(
                    item.Item(main.current_path, i, time.ctime(os.path.getmtime(main.current_path + '/' + i)),
                              os.path.getsize(main.current_path + '/' + i)))
            # item_dict = item.getItemJson(main.current_path)
            # item_dict_bytes = json.dumps(item_dict).encode('utf_8')
            # conn.sendall(item_dict_bytes)
        elif str.startswith(answer, 'exist:'):
            answer = answer[6:]
            existence = os.path.exists(answer)
            if existence:
                existence_bytes = 'T'.encode("utf_8")
            else:
                existence_bytes = 'F'.encode("utf_8")
            conn.sendall(existence_bytes)
        elif str.startswith(answer, 'isdir:'):
            answer = answer[6:]
            isdir = os.path.isdir(answer)
            if isdir:
                isdir_bytes = 'T'.encode("utf_8")
            else:
                isdir_bytes = 'F'.encode("utf_8")
            conn.sendall(isdir_bytes)
        elif str.startswith(answer, 'file:'):
            answer = answer[5:]
            file = open(answer, 'rb')
            a = file.readlines()
            for i in a:
                conn.sendall(i)
            conn.sendall("finish,&*^".encode("utf_8"))
            file.close()


# for managing the clients who wants to see this system files
def createServerside(host,port):

    print("serverside is created", host , port)

    clients = []
    MAX_BUFFER_SIZE = 4098
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host,port))
    server_socket.listen(2)

    while True:
        print("serside is created")
        conn , addr = server_socket.accept()
        ip , port = str(addr[0]) , str(addr[1])
        clients.append(conn)
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_service,args=(conn, ip, port,clients)).start()
        except:
            print("Bad thing happend!")
            import traceback
            traceback.print_exc()





