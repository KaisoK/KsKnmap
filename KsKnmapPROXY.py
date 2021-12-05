from multiprocessing import Process, Queue
import socks
import socket
import subprocess
import requests

x = open("/home/kaisok/Documentos/Python/Onion/ListaPrueba", "r", encoding="latin-1")
url = x.readlines()
x.close()
subprocess.run("clear")

puertosAbiertos = []

def torrente(min, max):

    for i in url:
        nombre = i.strip("\n")
        i = i.split(" ")[1].strip("\n")

        for puerto in range(min, max):
            print("\nProbando puerto {}".format(puerto))

            try:

                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
                s = socks.socksocket()
                s.settimeout(2)
                address = (i, puerto)
                s.connect(address)
                
                print("-----Abierto-----")

                q.put(puerto)
                
                s.close()
                
            except:

                print("casi")

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

for i in url:
    nombre = i.strip("\n")
    i = i.split(" ")[1].strip("\n")

    for puerto in puertosAbiertos:
        
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
            s = socks.socksocket()
            s.settimeout(2)
            address = (i, puerto)
            s.connect(address)
            a = s.recv(1024).decode()
            s.close()

            if "SSH" in a:
                    print("\n#######################")
                    print("\n" + nombre)
                    print("\nEs SSH")
                    print("\n#######################")
                    
            elif "FTP" in a:
                print("\n#######################")
                print("\n" + nombre)
                print("\nEs FTP")
                print("\n#######################")

        except:

            try:

                print("\n#######################")
                proxies = {'http': 'socks5h://127.0.0.1:9050'}
                data = requests.head("http://{}:{}".format(i, puerto),proxies=proxies).headers
                if data["Server"]:
                    print("\nHTTP SERVER: {}".format(data["Server"]))
                else:
                    print("\nHTTP SERVER")
                print("\n#######################")

            except:

                print("\n#######################")
                print("\nOTRO SERVICIO")
                print("\n#######################")
