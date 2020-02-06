import datetime
from socket import socket
import threading
import logging

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


raddr = ('172.0.0.1',9999) # 服务端
client = socket()
client.connect(raddr)
while True :
    data = client.recv(1024)
    logging.info(data)
    if data.strip() == b'quit':
        break
    client.send(b'ack')

client.close()
