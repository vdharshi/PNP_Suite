import re
import os
import csv
import time
import Global_Var
print("Test Case ID PS_013: Check whether OS support writing invalid P-state to sysfs entry")
max_cpu=Global_Var.max_no_of_cores
ctr=0
ctr1=0
i=0
while i<max_cpu:
 print(f"for core {i}")
 with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq",'r') as f:
  set_freq=f.read()
 set=int(set_freq[:-1])-10000
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_min_freq",'w') as f:
  f.write(str(set))
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq",'w') as f:
  f.write(str(set))   
 with open("/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f:
  scaling_cur_freq=f.read()
 print(f"set_freq_LFM = {set}")
 print(f"scaling_cur_freq = {scaling_cur_freq}")
 if scaling_cur_freq == set:
  ctr=ctr+1
  print("SUCCESS: scaling_cur_freq is matching with invaild LFM for CPU{i}")
 else:
  print("FAILURE: scaling_cur_freq is not matching with invalid LFM for CPU{i}")
 print("----------------------------------------------------------------------------")
 i=i+1
i=0
while i<max_cpu:
 print(f"for core {i}")
 freq=os.popen("cat /proc/cpuinfo | grep -i "model name" | cut -f 2 -d '@' | tr -d '.GHz' | sort -u | tr -d ' '`").read()
 set_freq=int(freq)*10000
 set=set_freq+10000
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_min_freq",'w') as f:
  f.write(str(set))
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq",'w') as f:
  f.write(str(set))   
 with open("/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f:
  scaling_cur_freq=f.read()
 print(f"set_freq_HFM = {set}")
 print(f"scaling_cur_freq = {scaling_cur_freq}")
 if scaling_cur_freq == set:
  ctr1=ctr1+1
  print("SUCCESS: scaling_cur_freq is matching with invaild HFM for CPU{i}")
 else:
  print("FAILURE: scaling_cur_freq is not matching with invalid HFM for CPU{i}")
 print("----------------------------------------------------------------------------")
 i=i+1
if ctr==max_cpu and ctr1==max_cpu:
 print("PS_013:SUCCESS")
 data = ["p_states","PS_013","SUCCESS","OS support writing invalid P-state to sysfs entry"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("PS_013:FAILURE")
 data = ["p_states","PS_013","FAILURE","OS doesnt support writing invalid P-state to sysfs entry"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

 