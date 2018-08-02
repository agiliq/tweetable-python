import ipaddress

ip_addr = input('Enter an IPv6 address: ')
try:
    ipaddress.ip_address(ip_addr)
except ValueError:
    print('Invalid IP v6 address')
else:
    print('Valid IP v6 address')
