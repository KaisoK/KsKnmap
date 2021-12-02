from multiprocessing import Process, Queue
from datetime import datetime
import socks, socket, subprocess, requests, pyfiglet, sys

subprocess.run("clear")

ascii_banner = pyfiglet.figlet_format("KsKnmap")
OpenPorts = []
t1 = datetime.now()

print(ascii_banner)
url = input("IP to scan - ")
print("\n" + "-" * 50)
print("Scanning Target: " + url)
print("Scanning started at:" + str(t1))
print("-" * 50)


def KsKnmap(min, max):

    try:

        for port in range(min, max):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((url,port))

            if result == 0:
                print("Port {} is open".format(port))
                q.put(port)

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



PortsList = [1000, 1501, 2001, 2501, 3001]

if __name__ == "__main__":
    
    procs = []
    q = Queue()
    for i in range(4):
        proc = Process(target=KsKnmap, args=(PortsList[i],PortsList[i+1]))
        procs.append(proc)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

while not q.empty():
    OpenPorts.append(q.get())

t2 = datetime.now()
TotalT = t2-t1

print("\n" + "-" * 50)
print(OpenPorts)
print("\nScan completed in {}".format(TotalT))
print("-" * 50)