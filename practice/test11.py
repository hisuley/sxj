__author__ = 'pc'

#a small server
import socket

s = socket.socket()

host = s.getpeername
port = 1234
s.bind(host, sort)

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from ', addr
    c.send('Thank you for connecting')
    c.close()


import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect(host, port)
print s.recv(1024)

from SocketServer import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from :', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler


class Sever(ThreadingMixIn, TCPServer): pass

class Handle(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from :', addr
        self.wfile.write('Thank you for connecting')

    server = Sever((''. 1234), Handler)
    server.serve_forever( )


import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs=[s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r in s :
            c, addr = s.accept()
            print 'Got connection from ', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print r.getpeername(), 'disconnected'
            else:
                print data



import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host. port))

fdmap = {s.fileno(): s}

s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd = s.fileno():
            c, addr = s.accept()
            print 'Got connection from', addr
            p.register(c)
            fdmap[c.s.fileno()] = c
        elif event & select.POllIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print fdmap[fd].getpeername, 'disconnected'
                p.unregister[fd]
                del fdmap[fd]
        else:
            print data