import random
import os

seq = {}
class GreetServer(object):
    def __init__(self):
        pass

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def perintah(self,command=None):
    	command = command.split(" ")
    	if command[0]=="LIST":
    		listdir = os.listdir()
    		b=''
    		for i in range(len(listdir)):
    			b=b+listdir[i]+" "
    		return b
    	if command[0]=="DEL":
    		try:
    			a=os.remove(command[1])
    			return "File "+command[1]+" berhasil dihapus"
    		except OSError as error:
    			return "Delete file gagal"
    	if command[0]=="CREATE":
    		open(command[1], 'a').close()
    		return "file "+command[1]+" created"
    	if command[0]=="READ":
    		fd = os.open(command[1],os.O_RDWR)
    		ret = os.read(fd,128)
    		return ret.decode()
    	if command[0]=="UPDT":
    		try:
    			with open(command[1], "a") as myfile:
    				myfile.write("\n"+command[2])
    			return "update success"
    		except Exception:
    			return "update gagal"

    # def ping(name):
    # count=0
    # while True:
    #     try:
    #         ns = Pyro4.locateNS("localhost",7777)
    #         count=0
    #     except Exception as e:
    #         count+=1
    #         print("\nserver down count "+str(count))
    #         if count>2:
    #             os.exit(1)
    #     time.sleep(2)

    def central_heartbeat(self,client_seq,id_client):
        global seq
        try:
            # ns = Pyro4.locateNS("localhost",7777)
            if seq[str(id_client)]==client_seq:
                seq[str(id_client)]+=1
                client_seq+=1
                return client_seq
        except Exception as e:
            seq[str(id_client)]=0
            return 0
    
    def all_heartbeat(self,client_seq,id_client):
        global seq
        try:
            # ns = Pyro4.locateNS("localhost",7777)
            if seq[str(id_client)]==client_seq:
                seq[str(id_client)]+=1
                client_seq+=1
                return client_seq,seq
        except Exception as e:
            seq[str(id_client)]=0
            return 0,seq

if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('royyana'))
