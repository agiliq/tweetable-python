import socket as s, struct, time

def ntp(url):
    c = s.socket(2, 2)
    d = b'\x1b' + 47 * b'\0'
    c.sendto(d, (url, 123))
    d, address = c.recvfrom(1024)
    if d:
        t = struct.unpack('!12I', d)[10]
        t -= 2208988800
        return time.ctime(t), t
