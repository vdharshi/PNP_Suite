#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_016: Check whether OS supports displaying the POR governor")
cntr=0
i=0
while i<max_cpu:
 print(f"PS_016,The POR Governor for CPU{i}")
 with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_governor",'r') as f:
  current_governor=f.read()
 with open(Global_Var.result_path/'governors_current.txt','a') as f:
  f.write(current_governor[:-1])
  
 if current_governor[:-1]=='powersave' or current_governor[:-1]=='performance' :
  print("PS_16:SUCCESS")
  cntr=cntr+1
 else:
  print("PS_16:FAILURE")
 i=i+1
if cntr==max_cpu:
 data = ["p_states","PS_016","SUCCESS","OS supports displaying the POR governor"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["p_states","PS_016","FAILURE","OS doesnot support displaying the POR governor"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
