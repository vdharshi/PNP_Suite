#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_004: List the supported governors")
open(Global_Var.result_path/"check.csv",'w').close()
cntr=0
i=0
while(i<max_cpu):
  print(f"PS_004,Governors supported by CPU{i}")
  with open(Global_Var.result_path/"check.csv",'a') as f:
    r=os.popen(f"cat /sys/devices/system/cpu/cpu{i}/cpufreq/scaling_available_governors").read()
    f.write(r)
  print(r)
  i=i+1
d=os.path.getsize(Global_Var.result_path/"check.csv")
c=os.popen("cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors | uniq | tr ' ' ';'").read()
if d!=0:
  print("PS_004: SUCCESS")
  data = ["p_states","PS_004","SUCCESS",f"listing the available governors:{c}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("CS_001: FAILURE")
  data = ["p_states","PS_004","FAILURE","governors are not available"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
