import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 14532

server.bind((HOST, PORT))
server.listen()
print(f'Server escutando na porta: {PORT}')

clients = []
usernames = []
def sendMessage(message):
    for client in clients:
        client.send(message)

def handle(client, username):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                sendMessage(f'[{username}] {message}'.encode('utf-8'))
            else:
                raise Exception("Cliente desconectado")
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            sendMessage(f'{username} desconectou do servidor.'.encode('utf-8'))
            break


def receive():
    while True:
        client, address = server.accept()
        print(f'Conexão estabelecidade com {address}')

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"O usuário {username} se conectou no servidor! endereço: {address}")
        sendMessage(f"{username} entrou no chat.".encode('utf-8'))
        client.send('Conectado ao servidor!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client, username,))
        thread.start()

print("Servidor iniciado e esperando conexões....")
receive()