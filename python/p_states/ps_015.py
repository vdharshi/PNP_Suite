import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_013: Check whether OS support writing invalid P-state to sysfs entry")
cntr=0
i=0
while i<max_cpu:
 print(f"PS_015,P-state Transition latency for CPU{i}")
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/cpuinfo_transition_latency",'r') as f:
  print(f.read())
  data = f.read()
 if data!='\n':
  print("PS_15:SUCCESS")
  cntr=cntr+1
 else:
  print("PS_15:FAILURE")
 i=i+1
if cntr==max_cpu:
 data = ["p_states","PS_015","SUCCESS","Supports P-state transition latency"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_015","FAILURE","doesnot Support P-state transition latency"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
