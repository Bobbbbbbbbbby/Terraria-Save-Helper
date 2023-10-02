import socket
from time import sleep

global client_socket

def check_connection(ip, port):
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    send_confirm = "hello server".encode("utf-8")
    client_socket.send(send_confirm)
    recv_data = str(client_socket.recv(32))
    print(recv_data)
    client_socket.close()

if __name__ == "__main__":
    print("Kang Tao - Intelligent Electronics Solutions")
    for i in range
    