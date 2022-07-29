#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test case : kpm_006")
time.sleep(1)
with open("/sys/power/pm_print_times",'r') as f:
 pm=f.read()
print(f"pm_print_times {pm[:-1]}")
if pm[:-1]=='1':
 print("SUCCESS")
 data = ["kernel_pm","kpm_006","SUCCESS","pm_print_times is enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["kernel_pm","kpm_006","FAILURE","pm_print_times is disabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
