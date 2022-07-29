#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Executing DPM_003")
print("Test Case ID DPM_003: Whether All PCIe devices have PM features enabled or not (ASPM and L1 substates)")
print("cutting the lines from 'lspci -vvv' o/p, which has 'ASPM Disabled;' and saving it in ASPM_L1_disabled.txt")
x=os.popen("lspci -vvv | grep -i 'ASPM Disbled'").read()
with open(Global_Var.result_path/"ASPM_L1_Disabled.txt",'w+') as f:
 f.write(x)
time.sleep(5)
s=os.path.getsize(Global_Var.result_path/"ASPM_L1_Disabled.txt")
if s!=0:
 print("ASPM_L1_Disabled.txt is not empty")
 print("FAILURE")
 data=["Device_pm","DPM_003","FAILURE,All PCIe devices don't have ASPM features enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("ASPM_L1_Enabled.txt is empty")
 print("SUCCESS")
 data = ["Device_pm","DPM_003","SUCCESS,All PCIe devices have ASPM features enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
