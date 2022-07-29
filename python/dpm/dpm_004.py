#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Executing DPM_004")
print("Test Case ID DPM_004: LPC should have auto power management enabled")
power_gating_lpc=os.popen("cat /sys/kernel/debug/pmc_core/pch_ip_power_gating_status | grep -i lpc | awk '{print $7}'").read()
print(f"power_gating_lpc={power_gating_lpc[:-1]}")
if power_gating_lpc[:-1] =='Off':
 print("SUCCESS")
 data = ["Device_pm","DPM_004","SUCCESS,LPC's auto power management enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data=["Device_pm","DPM_004","FAILURE","LPC's auto power management is not enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
