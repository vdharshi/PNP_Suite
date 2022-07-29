#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_007")
print("Test Case ID display_007: Display DC6 support: check whether display  enter DC6 state  when display is On")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
time.sleep(2)
print("iteration:1 - saving the DC6 value  in varaible reg_val")
with open("/sys/kernel/debug/dri/0/i915_dmc_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "DC6" in line:
   reg_val=line[-2:-1]
   print("reg_val:",reg_val)
   break
time.sleep(60)
print("iteration:2 - saving the DC6 value in  varaible reg_val1")
with open("/sys/kernel/debug/dri/0/i915_dmc_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "DC6" in line:
   reg_val1 = line[-2:-1]
   print("reg_val1:",reg_val1)
   break
  
time.sleep(5)
if reg_val1 > reg_val:
    print('SUCCESS')
    data = ["display","display_007","SUCCESS","Display enters DC6 state  when display is On"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_007","FAILURE","Display is not entering  DC6 state  when display is On"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
