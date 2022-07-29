import os
import sys
import csv
import struct
import Global_Var
def rdmsr(address,cpu=0):
        with open('/dev/cpu/0/msr','rb')as f:
         f.seek(address)
         return struct.unpack('=Q',f.read(8))[0]

x=rdmsr(0x772)
print(x)
x=x>>12
y=1
c=x & y
if c==1:
 print("EPP is supported by the platform")
 print("SUCCESS")
 data=["Device_pm","DPM_042","SUCCESS","EPP is supported by the platform"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("EPP is not supported by the platform")
 print("FAILURE")
 data = ["Device_pm","DPM_042","FAILURE","EPP is not supported by the platform"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

