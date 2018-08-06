import ipaddress

ip_addr = input('Enter an IPv4 address: ')
try:
    ipaddress.ip_address(ip_addr)
except ValueError:
    print('Invalid IP address')
else:
    print('Valid IP address')
