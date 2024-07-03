import socket
import threading

HOST = '127.0.0.1'
PORT = 14532

username = input("Digite seu nome de usuário: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Encerrando conexão com o servidor...")
            client.close()
            break

def write():
    while True:
        try:
            message =  input("")
            client.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            print('Encerrando o cliente...')
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write()