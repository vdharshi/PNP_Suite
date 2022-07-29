#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_025")
print("Test Case ID display_025: checks whether current CD clock frequency = 307200kHz")
with open("/sys/kernel/debug/dri/0/i915_frequency_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  stat='/n'
  if "Current CD clock frequency" in line:
   freq=line[-11:-1]
   print(freq)
   break
   
if freq == '307200 kHz':
    print('SUCCESS')
    data = ["display","display_025","SUCCESS",f"CD clock frequency = {freq}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_025","FAILURE",f"CD clock frequency = {freq} not 307200kHz"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
