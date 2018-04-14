import socket,item,main,json,time,os,json,threading
from threading import Thread

lock = threading.Lock()

class Server:
    def __init__(self,_host,_port):
        self.host = _host
        self.port = _port
        self.serverSocket = socket.socket()
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(2)
        self.MAX_BUFFER_SIZE=4098
        self.clients={}

    def start(self):
        while True:
            print("main server is waiting")
            conn,addr = self.serverSocket.accept()
            ip= str(addr[0])
            print("new client added")
            Thread(target=self.recive , args=(conn,ip)).start()

    def recive(self,conn,ip):
        while True:
            answer_in_bytes = conn.recv(self.MAX_BUFFER_SIZE)
            answer = answer_in_bytes.decode('utf_8')

            if str.startswith(answer,"info:"):
                info = answer[5:]
                clientInfo=info.split(',&*^')
                name=clientInfo[0]
                personalPort = int(clientInfo[1])
                self.clients[name] = {"conn":conn,"ip":ip,"personalPort":int(personalPort)}
                self.updateClientsData()
                
    def updateClientsData(self):
        dic = {}
        for client in  self.clients:
            dic[client]={"ip":self.clients[client]["ip"],"personalPort":self.clients[client]["personalPort"]}
        dic_bytes = json.dumps(dic).encode("utf_8")
        for client in self.clients:
            with lock:
                print(dic)
            conn = self.clients[client]["conn"]
            conn.sendall(dic_bytes)
