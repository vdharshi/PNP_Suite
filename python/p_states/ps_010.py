import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_010: The OS shall support setting P-state to LFM")
cntr=0
i=0
set_freq=os.popen("cat /proc/cpuinfo | grep -i 'model name' | cut -f 2 -d '@' | tr -d '.GHz' | sort -u | tr -d ' '").read()
set_freq=int(set_freq)
set_freq=set_freq*10000
print(set_freq)
while i<max_cpu:
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq",'w') as f:
  f.write(str(set_freq))
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_min_freq",'w') as f:
  f.write(str(set_freq))   
 time.sleep(1)
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f:
  scaling_cur_freq=f.read()
  scaling_cur_freq=int(scaling_cur_freq[:-1])

 print(f"set_freq_LFM = {set_freq}")
 print(f"scaling_cur_freq = {scaling_cur_freq}")
 a=set_freq+100000
 b=set_freq-100000
 if scaling_cur_freq <= a and scaling_cur_freq>=b:
  print(f"SUCCESS:scaling_cur_freq is matching with LFM for CPU{i}")
  cntr=cntr+1
 else:
  print(f"FAILURE:scaling_cur_freq is not matching with LFM for CPU{i}")
 i=i+1
if max_cpu == cntr:
 print("SUCCESS")
 data = ["p_states","PS_010","SUCCESS","scaling_cur_freq is matching with LFM for CPU"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["p_states","PS_010","FAILURE","scaling_cur_freq is not matching with LFM for CPU" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
