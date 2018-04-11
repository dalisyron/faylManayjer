import socket,item,main,json,time,os
from threading import Thread

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
            conn,addr = self.server_socket
            ip= str(addr[0])
            print("new client added")
            Thread(target=self.recive , args=(conn,ip)).start()

    def recive(self,conn,ip):
        while True:
            answer_in_bytes = conn.recv(self.MAX_BUFFER_SIZE)
            answer = answer_in_bytes.decode('utf_8')

            if str.startswith(answer,"name:"):
                name = answer[5:]
                self.clients[name] = (conn , ip)
                self.updateClientsData()

            elif str.startswith(answer,"connect:"):
                #faghat name ro mifreste
                targetName = answer[8:]
                targetIp = self.clients[targetName][1]
                targetConn = self.clients[targetName][0]
                port = 9090 # /: be mola
                self.sendMakeServerRequest(targetConn,targetIp,port)#be target migim server sho.
                self.sendConnectToServerRequest(conn,targetIp,port)

    def sendMakeServerRequest(self,conn,host,port):
        message = "makeServer:" + ',&*^'.join([host,port])
        message_bytes = message.encode(message)
        conn.sendall(message_bytes)

    def sendConnectToServerRequest(self,conn,host,port):
        message = "connectTo:" + ',&*^'.join([host,port])
        message_bytes = message.encode(message)
        conn.sendall(message_bytes)

    def updateClientsData(self):
        message = "connectedList:"+',&*^'.join(self.clients.keys())
        message_bytes = message.encode()
        for client in self.clients:
            conn = self.clients[client][0]
            conn.sendall(message_bytes)
