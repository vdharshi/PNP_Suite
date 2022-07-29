#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores

print("Test Case ID PS_001: Check whether the OS supports cpufreq framework or not")
ctr=0
i=0
while i<max_cpu:
 path = (f"/sys/devices/system/cpu/cpu{i}")
 dir_list = os.listdir(path)

 if "cpufreq" in dir_list :
  ctr=ctr+1
  print(f"PS_001,SUCCESS: OS supports cpufreq framework for CPU{i}")
 else:
  print(f"PS_001,FAILURE: OS didn't support cpufreq framework for CPU{i}")
 i=i+1

if ctr==max_cpu:
 data = ["p_states","PS_001","SUCCESS","OS is supporting cpufreq framework"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_001","FAILURE","OS is not supporting cpufreq framework"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
