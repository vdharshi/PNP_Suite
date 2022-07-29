#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_028: Check the total number of core c-states")
print("Check the total number of core c-states")
time.sleep(2)
cc=os.popen("ls /sys/devices/system/cpu/cpu0/cpuidle | wc -l").read()
print(f"cc={cc}")
cc=int(cc[:-1])
open(Global_Var.result_path/'d.txt','w').close()
if cc>0:
 with open(Global_Var.result_path/"c.txt",'w+') as f:
  x=os.popen("ls /sys/devices/system/cpu/cpu0/cpuidle").read()
  f.write(x)
 with open(Global_Var.result_path/"c.txt",'r') as f:
  index=0
  for line in f:
   index=index+1
   with open(f"/sys/devices/system/cpu/cpu0/cpuidle/{line[:-1]}/name",'r') as f:
    w=f.read()
    with open(Global_Var.result_path/"d.txt",'a')as f:
     f.write(w)
 c=os.popen(f"cat {Global_Var.result_path}/d.txt | tr '\n' ' ' ").read()
 print("SUCCESS")
 data=["c_states","CS_028","SUCCESS",f"Total number of core c-states are {cc} which are {c}"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_028","FAILURE","NA"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
