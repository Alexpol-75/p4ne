import random
import ipaddress

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0b000000,0xdf000000), random.randint(8,24)), strict=False)
        self.regular = not self.is_private

L = []

while len(L) < 20:
    net = IPv4RandomNetwork()
    if net.regular: L.append(net)

#for i in L: print(i, i.regular)
for i in range(len(L)): print("#", i+1, "network: ", L[i], "regular:", L[i].regular)
