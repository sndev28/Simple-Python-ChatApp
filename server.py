import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import time


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = '!q'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print('[SERVER CREATED]    Server created!')

all_clients = []

class ClientRoom:
    client = ''
    room_no = ''
    def __init__(self, client, room_no):
        self.client = client
        self.room_no = room_no




def client_connection(conn, addr):
    room_no = conn.recv(1024).decode()
    clientObj = ClientRoom(conn, room_no)
    all_clients.append(clientObj)
    
    connected = True
    while connected:
        msg = conn.recv(1024).decode()
        if msg == DISCONNECT_MESSAGE:
            connected = False

        message = f'{time.asctime(time.localtime(time.time()))} {msg}'

        for client in all_clients:
            if client.room_no == room_no:
                client.client.send(message.encode())

    all_clients.remove(conn)
    conn.close()

        

def start_server():
    server.listen()
    print(f'[SERVER LISTENING]   Server listening on {HOST}:{PORT}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = client_connection, args = (conn, addr))
        thread.start()


        print(f'[CLIENT CONNECTED]   Active clients: {threading.activeCount() - 1}')


if __name__ == '__main__':
    start_server()

