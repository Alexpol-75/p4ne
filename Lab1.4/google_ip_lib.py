import ipaddress
ip1 = ipaddress.IPv4Address('192.168.0.1')

print( ip1.is_private )
print( ip1.is_link_local )
print( ip1.is_multicast )
print( ip1.version )
print( ip1.reverse_pointer)

print( int(ip1) )           #decimal
print( "%x" % int(ip1) )    #hex

net1 = ipaddress.IPv4Network("192.168.1.0/24")
net2 = ipaddress.IPv4Network((ip1,24), strict=False)
print(net1)
print(net2)

print('\n************ ALL net IP\n')
for ip in net1:
    print(ip," ", end='')

print('\n************ hosts:\n')
for ip in net1.hosts():
    print(ip," ", end='')

print('\n\n******', net1.prefixlen, net1.network_address)

# IPv4Interface