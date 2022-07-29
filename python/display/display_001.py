#!/usr/bin/python3
import os
import sys
import csv
import Global_Var
print("Executing display_001")
print("Test Case ID display_001: checks whether display frequency = 60")
freq=os.popen("cat /sys/kernel/debug/dri/0/i915_display_info | grep mode | head -1 | cut -f5 -d ' '| tr -d ':'").read()
freq=freq[:-1]
print(freq)
if freq == '60':
  print("SUCCESS")
  data = ["display","display_001","SUCCESS",f" display frequency is {freq}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["display","display_001","FAILURE",f"display frequency is {freq} not 60"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
