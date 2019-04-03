import socket
from datetime import datetime
import threading
from queue import Queue


print_lock = threading.Lock()

# host = input("Enter a remote host to scan: ")
host = "www.info.nitk.ac.in"
ip = socket.gethostbyname(host)

print("-" * 80)
print("              Please wait, scanning the host --------> ", ip)
print("-" * 80)

t1 = datetime.now()

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("\n Port %d Is Open!!!!!!!!!!!!!" %(port))
            sock.close()
        else:
            print("\n Port %d Is Close :( " %(port))
            
    except:
        pass

def threader():
    while True:
        worker = q.get()

        scan(worker)

        q.task_done()



q = Queue()

for x in range(60):
     t = threading.Thread(target=threader)

     t.daemon = True

     t.start()

for worker in range(1,100):
    q.put(worker)

q.join()

t2 = datetime.now()
total = t2 - t1
print('Scanning Completed in: ', total)