#sockets
from socket import socket, AF_INET, SOCK_DGRAM
from gamePlay import *

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000 # servidor
HOST = '127.0.0.1' # servidor




def client():

    text = "Qual o sentido da vida ?"
    data = text.encode(ENCODE)

    sock = socket(AF_INET, SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)
    print("Mensagem enviada, esperando resposta")

    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode(ENCODE)
    print("A resposta foi: " + text)

    while True:
        menu()
        texto = int(input(" Escolha a opção desejada: "))
        data = texto.encode(ENCODE)
        sock = socket(AF_INET, SOCK_DGRAM)
        dest = (HOST, PORT)
        sock.sendto(data, dest)
        print("Mensagem enviada, esperando resposta")
        
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        print("A resposta foi: " + text)

    

if __name__ == "__main__":
    client()