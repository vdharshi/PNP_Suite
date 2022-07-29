#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_029: Check whether the core c-states are intel enabled")
time.sleep(2)
with open(Global_Var.result_path/"cc.txt",'w')as f:
 s=os.popen("cat /sys/devices/system/cpu/cpu0/cpuidle/state1/name | grep ACPI").read()
 f.write(s)
c=os.path.getsize(Global_Var.result_path/"cc.txt")
if c!=0:
 print("FAILURE")
 data=["c_states","CS_029","FAILURE","core c-states are not intel enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("SUCCESS")
 data = ["c_states","CS_029","SUCCESS","core c-states are intel enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
