#sockets
from cm_negocio import CampoMinado
from socket import socket, AF_INET, SOCK_DGRAM

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000 #cleinte
HOST = '127.0.0.1' #cliente

def server():

    orig = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(orig)
    camp = CampoMinado()

    while True:
        print("Ativando servidor ... ")
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        print("Recebemos a seguinte pergunta: " + text)
        if text



        text = "42"
        data = text.encode(ENCODE)
        sock.sendto(data, address)

if __name__ == "__main__":
    server()
            