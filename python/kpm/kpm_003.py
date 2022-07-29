#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test case : kpm_003 PM core should support reading the current number of registered wakeup events.")
with open("/sys/power/wakeup_count") as f:
 actual_var=f.read()
print(f"act:{actual_var[:-1]}")
with open(Global_Var.func_config_path/"mofd_config.csv",'r') as f:
 for line in f:
  if re.search("kpm_003",line):
   x=line
expected_var=x[8:9]
print(f"exp:{expected_var}")
if actual_var >= expected_var:
 print("SUCCESS")
 data = ["kernel_pm","kpm_003","SUCCESS",f"Actual_res_wakeupcount:{actual_var[:-1]}"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["kernel_pm","kpm_003","FAILURE","Actual_res_wakeupcount:{actual_var[:-1]}"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

