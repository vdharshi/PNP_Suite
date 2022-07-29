#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_011: Check whether OS supports checking the minimum scaling P-state")
cntr=0
i=0
while i<max_cpu:
 print(f"PS_011,Minimum P-state supported by the POR governor for CPU{i}")
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_min_freq",'r') as f:
  print(f.read())
  data = f.read()
  with open(Global_Var.result_path/f'check{i}.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 s=os.path.getsize(Global_Var.result_path/f'check{i}.csv')
 if s>0:
  print("PS_11:SUCCESS")
  cntr=cntr+1
 else:
  print("PS_11:FAILURE")
 i=i+1
if cntr==max_cpu:
 data = ["p_states","PS_011","SUCCESS","OS supports checking the minimum scaling P-state"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_011","FAILURE","OS doesnot support checking the minimum scaling P-state"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
