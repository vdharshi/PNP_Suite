#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_002: List Supported frequencies by the platform")
flag=0
ctr=0
i=0
while i<max_cpu:
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f:
  freq=f.read()
 if ' ' == freq:
  flag=flag+1
 else:
  with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_cur_freq",'r') as f: 
   check=f.read()
  with open(Global_Var.result_path/f'check_{i}.txt','w+') as f:
   f.write(check)
 sz = os.path.getsize(Global_Var.result_path/f"check_{i}.txt")
 if sz>0:
   ctr=ctr+1
   data=(f"Frequencies supported by cpu{i},{freq[:-1]}")
   with open(Global_Var.result_path/"logs_PS_002.txt",'w+') as f:
    f.write(data)
 else:
    data=(f"Frequencies aren't supported by cpu{i},{freq[:-1]}")
    with open(Global_Var.result_path/"logs_PS_002.txt",'w+') as f:
     f.write(data)
 i=i+1
if flag == max_cpu:
 data = ["p_states","PS_002","FAILURE","Scaling frequencies is not available"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data) 
elif ctr==max_cpu:
 data = ["p_states","PS_002","SUCCESS","Frequencies supported by cpu"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data) 
else:
 data = ["p_states","PS_002","FAILURE","Frequencies are not supported by cpu"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data) 
     
