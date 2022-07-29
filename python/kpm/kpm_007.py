#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test case : kpm_007")
with open("/sys/power/pm_freeze_timeout") as f:
  pm=f.read()
print(f"pm_freeze_timeout :{pm[:-1]}")
with open(Global_Var.func_config_path/"mofd_config.csv",'r') as f:
 for line in f:
  if re.search("kpm_007",line):
   x=line
   n=len(line)
expec_timeout=x[8:n-1]
print(f"expec_timeout :{expec_timeout}")
if pm[:-1] == expec_timeout:
 print("SUCCESS")
 data = ["kernel_pm","kpm_007","SUCCESS",f"Exp_freeze_timeout : {expec_timeout}; Actual_freeze_timeout :{pm[:-1]}"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["kernel_pm","kpm_007","FAILURE","Exp_freeze_timeout : {expec_timeout}; Actual_freeze_timeout :{pm[:-1]}"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

