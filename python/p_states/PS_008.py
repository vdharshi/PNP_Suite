#!/usr/bin/python3
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_008: Check whether the OS supports checking the Maximum P-state of the platform")
cntr=0
i=0
while i<max_cpu:
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/cpuinfo_max_freq",'r') as f:
  cmax=f.read()
 cmax=int(cmax)
 if cmax>0:
  cntr=cntr+1
  print(f"Maximum P-state for CPU{i} is {cmax}, SUCCESS")
 else:
  print(f"Maximum P-state for CPU{i}, FAILURE")
 i=i+1
if max_cpu == cntr:
 data = ["p_states","PS_008","SUCCESS","OS supports checking the maximum P-state of the platform"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_008","FAILURE","OS doesnot support checking the maximum P-state of the platform" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

 
