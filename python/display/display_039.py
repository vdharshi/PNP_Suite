#!/usr/bin/python3
import os
import sys
import csv
import time
import Global_Var
print("Executing display_039")
print("Test Case ID display_039: Display DC5 support: check whether display  enter DC5 state  when display is On")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
time.sleep(2)
print("iteration:1 - saving the DC5 value  in varaible reg_val")
reg_val=os.popen("cat /sys/kernel/debug/dri/0/i915_dmc_info | grep 'DC5 count' | cut -d ':' -f2 | tr -d ' '").read()
print("reg_val="+reg_val)
time.sleep(60)

print("iteration:2 - saving the DC5 value in  varaible reg_val1")
reg_val1=os.popen("cat /sys/kernel/debug/dri/0/i915_dmc_info | grep 'DC5 count' | cut -d ':' -f2 | tr -d ' '").read()
print("reg_val1="+reg_val1)
time.sleep(5)
if reg_val1[:-1] > reg_val[:-1]:
  print("SUCCESS")
  data = ["display","display_039","SUCCESS","Display enters DC5 state  when display is On"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["display","display_039","FAILURE","Display is not entering  DC5 state  when display is On"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
