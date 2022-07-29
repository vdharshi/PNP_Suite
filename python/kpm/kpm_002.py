#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test case : kpm_002")
time.sleep(1)
with open("/sys/power/pm_async",'r') as f:
 pm=f.read()
print(pm[:-1])
if pm[:-1]=='1':
 print("SUCCESS")
 data = ["kernel_pm","kpm_002","SUCCESS","pm_async is enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["kernel_pm","kpm_002","FAILURE","pm_async is disabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
