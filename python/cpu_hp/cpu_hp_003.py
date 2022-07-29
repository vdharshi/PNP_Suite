#!/usr/bin/python3
import csv
import Global_Var
import os  
print("Test case :  cpu_hp_003")
with open("/sys/devices/system/cpu/cpuidle/current_driver",'r') as f:
 current_driver=f.readline()
with open("/sys/devices/system/cpu/cpuidle/current_governor_ro",'r') as f:
 current_governor_ro=f.readline()

with open(Global_Var.result_path/'check.csv', 'a')as f: 
  writer = csv.writer(f)
  writer.writerow(current_governor_ro)
sz = os.path.getsize(Global_Var.result_path/'check.csv')
if (sz>0):
  data = ["cpu_hotplug","cpu_hp_003","SUCCESS",f'current_driver = {current_driver[:-1]} , current_governor_ro = {current_governor_ro[:-1]}']
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  data = ["cpu_hotplug","cpu_hp_003","FAILURE,SYfs entry dont exist for cpu driver and governer"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
