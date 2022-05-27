class Subnet:
    def __init__(self, n='0.0.0.0', p='/24'):
        self.network = n
        self.prefix = p
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix
    def __str__(self):
        return self.network+self.prefix
    def __repr__(self):
        return self.network+self.prefix

class Addr_plan_entry(Subnet):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        Subnet.__init__(self,n,p)
        self.gateway = gw
    def getgw(self):
        return self.gateway

n1 = Subnet("192.168.1.0","/24")
n2 = Subnet("172.16.0.0","/16")
n3 = Subnet()

print(type(n1), n1, dir(n1))
print(type(n2), n2, n2.getnet(),n2.getprefix())
print(type(n3), n3)

L = [n1, n2]
print(L)
print(L[0])

ap1 = Addr_plan_entry("192.168.1.0","/24","192.168.1.1")
print(dir(ap1))
print(ap1.__dict__)  # Вернуть все поля класса в виде словаря dict
print('\n',ap1.getgw())