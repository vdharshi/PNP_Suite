import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_009: The OS shall support setting P-state to LFM")
cntr=0
i=0
while i<max_cpu:
 with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq",'r') as f:
  set_freq=f.read()
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq",'w') as f:
  f.write(set_freq)
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_min_freq",'w') as f:
  f.write(set_freq)   
 time.sleep(1)
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f:
  scaling_cur_freq=f.read()
  scaling_cur_freq=int(scaling_cur_freq[:-1])
 set_freq=int(set_freq[:-1])
 print(f"set_freq_LFM = {set_freq}")
 print(f"scaling_cur_freq = {scaling_cur_freq}")
 a=set_freq+100000
 b=set_freq-100000
 if scaling_cur_freq <= a and scaling_cur_freq>=b:
  print(f"scaling_cur_freq is matching with LFM for CPU{i}")
  cntr=cntr+1
 else:
  print(f"scaling_cur_freq is not matching with LFM for CPU{i}")
 i=i+1
print(max_cpu,cntr)
if max_cpu == cntr:
 data = ["p_states","PS_009","SUCCESS","scaling_cur_freq is matching with LFM for CPU"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_009","FAILURE","scaling_cur_freq is not matching with LFM for CPU" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
