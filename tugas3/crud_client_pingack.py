import Pyro4
import threading
import time
import os

def test_no_ns():
    uri = "PYRO:obj_27d7c59497c44c688319f7d8a4a95935@localhost:40549"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def test_with_ns():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def CRUD(command=None):
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.perintah(command))

def ping(name):
    count=0
    while True:
        try:
            ns = Pyro4.locateNS("localhost",7777)
            count=0
        except Exception as e:
            count+=1
            print("\nserver down count "+str(count))
            if count>2:
                os._exit(1)
        time.sleep(2)

if __name__=='__main__':
    x = threading.Thread(target=ping, args=(1,))
    x.start()
    while True:
        command = input("Command : ")
        CRUD(command)
