import socket
from multiprocessing import Process
from tcp_server import startServer

global process
global process_port

def createServer(port=6666, maxListen=16):
    global process
    global process_port
    process = Process(target=startServer, args=(port, maxListen))
    process_port = port
    process.start()

def endServer():
    global process_port
    mngSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mngSocket.connect(("127.0.0.1", process_port))

    phase1Send = "admin;manager;344455;".ljust(32, ' ').encode()
    phase2Send = "end:".ljust(32, ' ').encode()

    mngSocket.send(phase1Send)
    mngSocket.send(phase2Send)
    phase3Recv = mngSocket.recv(512).decode().split(';')[0]
    print("Server respond: " + phase3Recv)

def checkServer():
    global process
    if process.is_alive() is True:
        print('server is still alive')
    else:
        print('server is not alive')