#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Executing DPM_007")
print("check whether the pci devices /power/runtime_status is suspended or not")
a=0
b=0
open(Global_Var.result_path/'runtime_status_active.txt','w').close()
open(Global_Var.result_path/'runtime_status_suspended.txt','w').close()
x=os.popen("lspci | cut -d ' ' -f1  | sed 's/0/0000:0/'").read()
with open(Global_Var.result_path/'pci.txt','w+')as f:
 f.write(x)
with open(Global_Var.result_path/'pci.txt','r')as f:
 index=0
 for line in f:
  index=index+1
  print(f"runtime status for {line}")
  s=os.popen(f"cat /sys/bus/pci/devices/{line[:-1]}/power/runtime_status").read()
  if s[:-1]=='active':
   a=a+1
   with open(Global_Var.result_path/'runtime_status_active.txt','a')as f:
    f.write(line)
  else:
   b=b+1
   with open(Global_Var.result_path/'runtime_status_suspended.txt','a')as f:
    f.write(line)
print(f"Runtime suspend devices =  {b}")
print(f"Runtime active devices  =  {a}")
d=a+b
if b!=0:
 print("SUCCESS")
 data = ["Device_pm","DPM_007","SUCCESS",f"out of {d} PCI device; {b} devices are in runtime suspended state when in idle"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data=["Device_pm","DPM_007","FAILURE",f"{a} Device Drivers are not in runtime suspended state when in idle"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
 
