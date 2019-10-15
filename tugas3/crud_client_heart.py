import Pyro4
import threading
import time
import os
import uuid

seq=0
all_client_seq={}
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
                os.exit(1)
        time.sleep(2)

def heartbeat1(i,myid):
    global seq
    count=0
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    while True:
        try:
            uri = "PYRONAME:greetserver@localhost:7777"
            gserver = Pyro4.Proxy(uri)
            seq=gserver.central_heartbeat(seq,myid)
            print("seq "+str(seq))
        except Exception as e:
            print("server is down")
            if count>2:
                os.exit(1)
        time.sleep(2)

def heartbeat2(i,myid):
    global seq
    count=0
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    while True:
        try:
            uri = "PYRONAME:greetserver@localhost:7777"
            gserver = Pyro4.Proxy(uri)
            seq,all_client_seq=gserver.all_heartbeat(seq,myid)
        except Exception as e:
            print("server is down")
            if count>2:
                os.exit(1)
        time.sleep(2)
        print("All Client Seq: \n"+str(all_client_seq))

if __name__=='__main__':
    # PING ACK
    # x = threading.Thread(target=ping, args=(1,))
    # x.start()

    # HEARTBEAT CENTRALIZED
    # myid=uuid.uuid4()
    # x = threading.Thread(target=heartbeat1, args=(1,myid))
    # x.start()

    # HEARTBEAT ALL 
    myid=uuid.uuid4()
    x = threading.Thread(target=heartbeat2, args=(1,myid))
    x.start()
    while True:
        command = input("Command : ")
        CRUD(command)
