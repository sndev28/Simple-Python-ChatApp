import socket
import threading
import time


HOST = '192.168.1.36'
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
HEADER = 1024

def message_listener():
    while True:
        msg = client.recv(HEADER)
        print(msg.decode())

def message_sender():
    print('[CLIENT READY]')
    while True:
        msg = input()
        client.send(f'{name}: {msg}'.encode(FORMAT))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
name = input('Enter your name:')
room = input('Which room do you want to use: ')
client.send(f'room:__:room {room}'.encode())


if __name__ == '__main__':

    thread = threading.Thread(target = message_listener)
    thread.start()

    message_sender()
