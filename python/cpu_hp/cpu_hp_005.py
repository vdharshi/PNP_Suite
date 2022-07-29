#!/usr/bin/python3
import csv
import time
import Global_Var
print("Test case : cpu_hp_005")
print("List minimum, maximum and base CPU frequency")
with open("/sys/devices/system/cpu/cpu0/cpufreq/base_frequency",'r') as f:
 a=f.readline()
 print(a[:-1])
with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq",'r') as f:
 b=f.readline() 
 print(b[:-1])
with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq",'r') as f:
 c=f.readline()
 print(c[:-1])

if a[:-1]!= 0 and b[:-1]!= 0 and c[:-1]!=0:
  data = ["cpu_hotplug","cpu_hp_005","SUCCESS",f"min cpu freq={c[:-1]}; max cpu freq={b[:-1]} and base cpu freq={a[:-1]}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  data = ["cpu_hotplug","cpu_hp_005","FAILURE","Sys-fs NA"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 
