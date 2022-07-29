#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID CS_001: Verify whether the platform supports cpuidle framework or not")
cpu_core=Global_Var.max_no_of_cores
ctr=0
i=0
while(i<cpu_core):
 with open(Global_Var.result_path/f"cpu{i}.txt",'w+') as f:
  x=os.popen(f"ls /sys/devices/system/cpu/cpu{i}").read()
  f.write(str(x))
 with open(Global_Var.result_path/f"cpu{i}.txt",'r') as f:
  for line in f:
   if re.search("cpuidle",line):
    actual_var=line
 with open(Global_Var.func_config_path/"mofd_config.csv",'r') as f:
  for line in f:
   if re.search("CS_001",line):
    n=len(line)
    expected_var=line[7:n-1]
  print(f"for {i} core;actual={actual_var[:-1]},expected={expected_var}")
 if actual_var[:-1] == expected_var :
  ctr=ctr+1
 i=i+1
if ctr==cpu_core:
  print("CS_001: SUCCESS")
  data = ["c_states","CS_001","SUCCESS","Platform supports cpuidle framework"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("CS_001: FAILURE")
  data = ["c_states","CS_001","FAILURE","Platform doesn't supports cpuidle framework"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
 
