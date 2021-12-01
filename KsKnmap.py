from multiprocessing import Process, Queue
from datetime import datetime
import socks, socket, subprocess, requests, pyfiglet, sys

subprocess.run("clear")

ascii_banner = pyfiglet.figlet_format("KsKnmap")
puertosAbiertos = []

print(ascii_banner)
url = input("IP to scan - ")
print("-" * 50)
print("Scanning Target: " + url)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


def torrente(min, max):

    try:

        for puerto in range(min, max):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            address = (url, puerto)
            s.connect(address)
            q.put(puerto)
            s.close()

            result = s.connect_ex((target,port))

            if result == 0:
                print("Port {} is open".format(port))
                s.close()
                
    except KeyboardInterrupt:
        print("\n Exitting Program")
        sys.exit()

    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved")
        sys.exit()

    except socket.error:
        print("\n Server not responding")
        sys.exit()



ListaPuertos=[1000, 1501, 2001, 2501, 3001]

if __name__ == "__main__":
    
    procs = []
    q = Queue()
    for i in range(4):
        proc = Process(target=torrente, args=(ListaPuertos[i],ListaPuertos[i+1]))
        procs.append(proc)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

while not q.empty():
    puertosAbiertos.append(q.get())

print(puertosAbiertos)