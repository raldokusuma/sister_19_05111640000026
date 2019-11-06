import os
import base64
import Pyro4

serverlist=[]
class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000',location=''):
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        nama=location+'/'+nama
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')

    def read(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        try:
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
            
    def update(self,name='filename000',content='',location=''):
        nama='FFF-{}' . format(name)
        nama=location+'/'+nama
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            content=content.encode()
            content = base64.b64decode(content)
            f.write(content)
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000',location=''):
        nama='FFF-{}' . format(name)
        nama=location+'/'+nama
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')

    def add_server(self,server_name):
        serverlist.append(server_name)

    def get_serverlist(self):
        return serverlist

    def fserver_object(self,servername):
        uri = "PYRONAME:{}@localhost:7777".format(servername)
        replserver = Pyro4.Proxy(uri)
        return replserver

    def consistency(self,from_server,command,filename,content=None):
        if command=="create":
            for server in serverlist:
                if str(server) != str(from_server):
                    print(str(server))
                    fserver=self.fserver_object(server)
                    fserver.create(filename,0)
                    # self.create(filename,server)
        elif command=='delete':
            for server in serverlist:
                if str(server) != str(from_server):
                    fserver=self.fserver_object(server)
                    fserver.delete(filename,0)
                    # self.delete(filename,server)
        elif command=='update':
            for server in serverlist:
                if str(server) != str(from_server):
                    fserver=self.fserver_object(server)
                    fserver.update(filename,content,0)
                    # self.update(filename,content,server)
        return "ok"

        
                

if __name__ == '__main__':
    k = FileServer()
    print(k.create('f1'))
    print(k.update('f1',content='wedusku'))
    print(k.read('f1'))
#    print(k.create('f2'))
#    print(k.update('f2',content='wedusmu'))
#    print(k.read('f2'))
    print(k.list())
    #print(k.delete('f1'))

