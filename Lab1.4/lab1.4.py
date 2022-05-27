import random
import ipaddress

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0b000000,0xdf000000), random.randint(8,24)), strict=False)
        self.regular = not self.is_private

def keyfunc(net):
    return int(net.netmask) * 2**32 + int(net.network_address)

# Генерируем список сетей
L = []
while len(L) < 20:
    net = IPv4RandomNetwork()
    if net.regular: L.append(net)

# Печатаем список в оригинальном порядке
#for i in L: print(i, i.regular)
print('\n***** Unsorted:')
for i in range(len(L)): print("#", i+1, "network: ", L[i], "regular:", L[i].regular)

# Сортируем и печатаем список снова
L.sort(key=keyfunc)
print('\n***** Sorted:')
for i in range(len(L)): print("#", i+1, "network: ", L[i], "regular:", L[i].regular)
