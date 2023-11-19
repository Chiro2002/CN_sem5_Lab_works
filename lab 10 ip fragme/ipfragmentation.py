import math
from prettytable import PrettyTable

print("IP FRAGMENTATION CALCULATOR")
size=int(input("Enter IP data packet size "))
mtu=int(input("Enter Size of MTU "))

if(size<20 or mtu<20):
    print("INVALID ARGUMENTS")
    exit()

if(size<mtu):
    print("Since MTU > IP data packet, the packet moves on to the next encapsulation phase without fragmentation")
    exit()

n=math.ceil((size-20)/(mtu-20))
print("Number of fragments made: ",n)
offset=((mtu-20)//8)
payload=offset*8
myTable = PrettyTable(["Fragment Number", "Fragment Size", "MF", "Offset (Ahead)"])
for i in range(n):
    if(i==0):
        myTable.add_row([str(i+1),str(payload)+" + 20 = "+str(payload+20), "1", "0"])    
    elif(i==(n-1)):
        myTable.add_row([str(i+1),str(size-payload*i)+" + 20 = "+str(payload+20), "0", str(offset*i)])
    else:
        myTable.add_row([str(i+1),str(payload)+" + 20 = "+str(payload+20), "1", str(offset*i)])
print(myTable)