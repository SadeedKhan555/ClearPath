# -*- coding: utf-8 -*-


import sys
import socket
import struct
#import pyModeS as pms

read = 49001
write = 49000

index = 0
freq = 2
ip = '10.33.130.99'
port = write
cmd = b'RREF'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))


path = 'Aircraft/Laminar Research/Cessna 172 SP/Cessna_172SP.acf'
plane_index = 1

   
   
acf1 = struct.pack('<4sxi150s2xi', b'ACFN',
                  plane_index,           # 0 -> User aircraft, otherwise 1-19
                  path.encode('utf-8'),  # remember to encode string as bytes
                  1)              # livery index for aircraft
sock.sendto(acf1, (ip, port) )


sock.close()