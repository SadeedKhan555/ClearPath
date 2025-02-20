# -*- coding: utf-8 -*-

import sys
import socket
import struct

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
                  path.encode('utf-8'))

# Send aircraft selection command
sock.sendto(acf1, (ip, port))

# Function to set throttle and move the plane forward
def set_throttle(throttle_value):
    """Sets throttle to move the plane forward."""
    dataref = b'DREF'
    throttle_dataref = b'sim/flightmodel/engine/ENGN_thro'
    data = struct.pack('<4sif100s', dataref, 0, throttle_value, throttle_dataref)
    sock.sendto(data, (ip, port))

# Set throttle to 0.8 (80% power)
set_throttle(0.8)
