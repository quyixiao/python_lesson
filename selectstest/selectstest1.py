import selectors
import socket


selectors.EVENT_WRITE


sel = selectors.DefaultSelector()


def accept(socket: socket.socket, mask):
    conn, addr = socket.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    """mask : 事情掩码的或值 """
    data = conn.recv(1000) # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)          #Hope it wont block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


socket = socket.socket()
socket.bind('localhost', 1234)
socket.listen(100)
socket.setblocking(False)

key = sel.register(socket, selectors.EVENT_READ, accept)
# fileobj,
# fd
# events
# data == read,accept

while True:
    events = sel.select() # 阻塞
    for key,mask in events:
        callback = key.data # a
        callback(key.fileobj,mask) # a(socket,mask)

