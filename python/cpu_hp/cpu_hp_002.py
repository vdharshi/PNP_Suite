#!/usr/bin/python3
import csv
import Global_Var
import os  
print("Test case :  cpu_hp_002")

with open("/sys/devices/system/cpu/possible",'r')as a:
 possible=a.readline()
 print("possible:",possible[:-1])
with open(Global_Var.result_path/'check.csv', 'a')as f: 
  writer = csv.writer(f)
  writer.writerow(possible[:-1])
sz = os.path.getsize(Global_Var.result_path/'check.csv')
if (sz>0):
  print("SUCCESS")
  data = ["cpu_hotplug","cpu_hp_002","SUCCESS",f"Possible core :{possible[:-1]} "]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["cpu_hotplug","cpu_hp_002","FAILURE",f"Possible core :{possible[:-1]}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
