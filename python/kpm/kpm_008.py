#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test case : kpm_008,Support all wakeup sources")
with open("/sys/kernel/debug/wakeup_sources",'r') as f:
 data=f.readlines()
with open(Global_Var.result_path/"kpm_008.txt",'w+') as f:
 data=str(data)
 f.write(data)
s=os.path.getsize(Global_Var.result_path/"kpm_008.txt")
if s != '/n':
 print("SUCCESS")
 data = ["kernel_pm","kpm_008","SUCCESS","supporting all wakeup sources"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["kernel_pm","kpm_008","FAILURE","not supporting all wakeup sources"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
