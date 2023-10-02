import socket

global keepWorking

def startServer(port, maxListen):
    global keepWorking
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "0.0.0.0"
    serverSocket.bind((host, port))
    serverSocket.listen(maxListen)

    keepWorking = True

    while keepWorking is True:
        clientSocket, addr = serverSocket.accept()
        phase1Recv = clientSocket.recv(32).decode()
        phase2Recv = clientSocket.recv(32).decode()

        phase3Send = handleRecv(phase1Recv, phase2Recv).ljust(512, ' ').encode()
        clientSocket.send(phase3Send)
        clientSocket.close()

def handleRecv(phase1Recv, phase2Recv):
    global keepWorking
    senderType, senderName, senderPasswd = parsePhase1(phase1Recv)
    command, arg = parsePhase2(phase2Recv)
    if (senderType == 'admin') and (senderName == 'manager') and (senderPasswd == '344455'):
        if command == 'end':
            keepWorking = False
            return 'finised;'

def parsePhase1(phase1Recv):
    userInfo = phase1Recv.split(';')
    return userInfo[0], userInfo[1], userInfo[2]

def parsePhase2(phase2Recv):
    commandLine = phase2Recv.split(':')
    # TODO multi arg support
    return commandLine[0], commandLine[1]