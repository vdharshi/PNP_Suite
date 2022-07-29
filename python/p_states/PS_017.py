#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_017: Check whether Related CPU interface is working as expected or not")
cntr=0
i=0
while i<max_cpu:
 with open("/sys/devices/system/cpu/cpu0/cpufreq/related_cpus",'r') as f:
  avail_cpu=f.read()
 with open("/sys/devices/system/cpu/cpu1/online",'w') as f:
  f.write("0")
 with open("/sys/devices/system/cpu/cpu0/cpufreq/related_cpus",'r') as f:
  offline_cpu=f.read()
 i=i+1
if avail_cpu==offline_cpu:
 data = ["p_states","PS_017","SUCCESS","Related CPU interface is working as expected"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_017","FAILURE","Related CPU interface is not working as expected"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
