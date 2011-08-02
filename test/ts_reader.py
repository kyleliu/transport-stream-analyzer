from struct import *

def ts2Hex(char):
    return (unpack('h',char+' ')[0] & 0xff)

def tsPacketHeader(packet):
    for i in range(0,187):
        print "\tindex " + ("%03d"%i) + ": " + ("%02x"%packet[i])

index = 0
length = 0
stream = []
startArr = []

f = open('new.ts','r')

char = f.read(1)
while (ts2Hex(char)>=0x00):
    length += 1;
    stream.append(ts2Hex(char))
    char = f.read(1)

print 'len: ' + str(length)

for byte in stream:
    if (0x47 == byte):
        startArr.append(index)
    index += 1

for idx in startArr[:]:
    print "TS Packet " + str(idx)
    tsPacketHeader(stream[idx:])
        
f.close()
