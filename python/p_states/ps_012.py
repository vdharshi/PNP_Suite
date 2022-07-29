import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_012: Check whether OS supports checking the maximum scaling P-state")
cntr=0
i=0
while i<max_cpu:
 print(f"PS_012,Maximum P-state supported by the POR governor for CPU{i}")
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq",'r') as f:
  print(f.read())
  data = f.read()
  with open(Global_Var.result_path/f'check_cs12_{i}.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 s=os.path.getsize(Global_Var.result_path/f'check_cs12_{i}.csv')
 if s>0:
  print("PS_12:SUCCESS")
  cntr=cntr+1
 else:
  print("PS_12:FAILURE")
 i=i+1
if cntr==max_cpu:
 data = ["p_states","PS_012","SUCCESS","OS supports checking the maximum scaling P-state"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_012","FAILURE","OS doesnot support checking the maximum scaling P-state"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
