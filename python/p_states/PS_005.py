#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_005: Check whether the Affected CPU interface is working as expected or not")
i=0
avail_cpu=0
while i<max_cpu:
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/affected_cpus",'r') as f:
  w=f.read()
  if w != '\n':
   avail_cpu=avail_cpu+1
 i=i+1
print(avail_cpu)
with open("/sys/devices/system/cpu/cpu1/online",'w') as f:
 f.write("0")
i=0
offline_cpu=0
while i<max_cpu:
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/affected_cpus",'r') as f:
  w=f.read()
  if w != '\n':
   offline_cpu=offline_cpu+1
 i=i+1
if avail_cpu>offline_cpu:
 data = ["p_states","PS_005","SUCCESS","Affected CPU interface is not working"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_005","FAILURE","Affected CPU interface is working as expected"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
