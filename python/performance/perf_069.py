#!/usr/bin/env
import os
import csv
import time
import Global_Var
print("Test Case ID perf_069: Check whether Hyper threading is enabled")
os.system(". /home/scripts/coreconfig.sh")

print(a)
print("offline cores:"+a)
if a=='0':
  print("all cores are online")
  print("making core 1 offline")
  os.system(". /home/scripts/coreconfig.sh off 1")
  b=os.popen(". /home/scripts/coreconfig.sh  on | grep -i offline | awk '{print $3}'").read()
  print("offline core:"+b)
  if b[0] == '1':
    print('SUCCESS')
    data = ["performance","perf_069","SUCCESS","Hyper threading is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
  else:
    print('FAILURE')
    data = ["performance","perf_069","FAILURE","Hyper threading is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
  print("Reboot the system")
  data = ["performance","perf_069","FAILURE","Reboot sysytem and run"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
