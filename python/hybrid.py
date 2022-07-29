#!/usr/bin/python3
import csv
import os
import time
import Global_Var
max_cpu=Global_Var.max_no_of_cores
print(max_cpu)
i=0
ctr=1
while i<max_cpu:
  with open(f"/sys/devices/system/cpu/cpu{i}/cpufreq/cpuinfo_max_freq",'r')as f:
    temp=f.read()
    print(temp)
  if i==0:
     c=temp[:-1]
  elif i>0 and c==temp[:-1]:
     ctr=ctr+1
     print(ctr)
  i=i+1

if ctr==max_cpu:
  print("SUCCESS")
else:
  print("FAILURE")        
