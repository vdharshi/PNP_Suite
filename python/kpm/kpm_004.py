#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Component: Kernel PM, ChromOS Power Policy settings")
os.popen("restart powerd")
time.sleep(10)
state=os.popen("power_supply_info | grep state | cut -d ':' -f 2 | tr -d ' '").read()
print(state[:-1])
if state[:-1]=="Fullycharged" or state =="Charging" :
 print("yes")
 dim_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 2 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(dim_time)
 screenoff_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 3 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(screenoff_time)
 sleep_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 6 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(sleep_time)
 if dim_time == "7m" and screenoff_time == "7m30s" and sleep_time== "8m30s":
  print("SUCCESS")
  data = ["kernel_pm","kpm_004","SUCCESS","It follows the Chrome OS Inactive Delay Power Policy"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 else:
  print("FAILURE")
  data = ["kernel_pm","kpm_004","FAILURE",f"DIM_time is {dim_time}; Screenoff_time is {screenoff_time}; sleep_time is {sleep_time}; It does not follows the Chrome OS Inactive Delay Power Policy"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
else:
 dim_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 2 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(dim_time)
 screenoff_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 3 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(screenoff_time)
 sleep_time=os.popen("cat /var/log/power_manager/powerd.LATEST | grep -i 'updated settings:' | tail -1 | cut -d '=' -f 6 | cut -d ' ' -f 1 | tr -d '[[:space:]]'").read()
 print(sleep_time)
 if dim_time == "5m" and screenoff_time == "5m30s" and sleep_time == "6m30s":
  print("SUCCESS")
  data = ["kernel_pm","kpm_004","SUCCESS","It follows the Chrome OS Inactive Delay Power Policy"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 else:
  print("FAILURE")
  data = ["kernel_pm","kpm_004","FAILURE",f"DIM_time is {dim_time}; Screenoff_time is {screenoff_time}; sleep_time is {sleep_time}; It does not follows the Chrome OS Inactive Delay Power Policy"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
 
