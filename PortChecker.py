import socket
import threading
from queue import Queue

target = input("Please Enter The Ip: ")
from_port = int(input("Please Enter First Range Of Port: "))
to_port = int(input("Please Enter Second Range Of Port: "))
thread = int(input("Please Enter The Threads: "))
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)



def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"[+] Port {port} Is Open")
            open_ports.append(port)

port_list = range(from_port, to_port)
fill_queue(port_list)

thread_list = []

for i in range(thread):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f"Open Ports Are: {open_ports}")
