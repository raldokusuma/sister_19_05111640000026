import os
import Pyro4
import base64

# repl_uri = "PYRONAME:repl_server@localhost:7777"
# replserver = Pyro4.Proxy(repl_uri)
servername=''
class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def replserver_object(self):
        uri = "PYRONAME:repl_server@localhost:7777"
        replserver = Pyro4.Proxy(uri)
        return replserver

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

    def create(self, name='filename000'):
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            
            replserver=self.replserver_object()
            replserver.consistency(servername,"create",name,None)
            return self.create_return_message('100','OK')
        except Exception as e:
            print(e)
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
            
    def update(self,name='filename000',content=''):
        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            replserver=self.replserver_object()
            replserver.consistency(servername,"delete",name,None)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')

    def add_servername(self,server_name):
        servername=server_name

    def get_servername(self):
        return servername


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

