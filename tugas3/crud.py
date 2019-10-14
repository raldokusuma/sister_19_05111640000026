import random
import os

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
    		

if __name__ == '__main__':
    k = GreetServer()
    print(k.get_greet('royyana'))
