#!/usr/bin/python3
import csv
import time
import Global_Var
print("Test case :  cpu_hp_001")
print("Checks whether it is possible to put cpu cores offline")
no_cpu_core=Global_Var.max_no_of_cores
print("no_cpu_core : ",no_cpu_core)
with open("/sys/devices/system/cpu/hotplug/states",'r') as f:
 for line in (f.readlines() [-1:]):
   on=line[0:3]
   print(on)
with open("/sys/devices/system/cpu/hotplug/states",'r') as f:
 off=f.readline()
 off=off[2:3]
 print(off)
i=0
while(i<no_cpu_core):
 with open(f"/sys/devices/system/cpu/cpu{i}/hotplug/state",'r') as f:
  state = f.readline()
 if state[:-1] == on:
  print(f"cpu{i} is in online by default")
 else:
  print(f"cpu{i} is in offline by default")
 i=i+1
i=0
ctr=0
while(i<no_cpu_core):
 print(f"Putting CPU{i} in offline....")
 time.sleep(10)
 
 with open(f"/sys/devices/system/cpu/cpu{i}/hotplug/target",'w') as f:
  f.write(off)
 with open(f"/sys/devices/system/cpu/cpu{i}/hotplug/state",'r') as f:
  state=f.readline()
 if state[:-1] == off:
   print(f"SUCCESS, Able to put cpu{i} in offline")
   ctr=ctr+1
 else:
   print(f"FAILURE, Unable to put cpu{i} in offline")
 print(f"putting CPU{i} in online....")
 with open(f"/sys/devices/system/cpu/cpu{i}/hotplug/target",'w') as f:
  f.write(on)
 print("-------------------------------------------------")
 i=i+1

if ctr== no_cpu_core:
  print("SUCCESS")
  data = ["cpu_hotplug","cpu_hp_001","SUCCESS","Able to put the cores in offline"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["cpu_hotplug","cpu_hp_001","FAILURE","Unable to put the cores in offline"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    
