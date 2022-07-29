#!/usr/bin/python3
import os
import Global_Var
import csv
import time
print("Test Case ID S0ix_001: The platform should support S0ix")
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count=a.readline()
 print("count=",count[:-1])
print("Please wait display will go off and wake after 1 minute")
with open ("/var/lib/power_manager/suspend_to_idle", 'w') as a:
 a.write("1")
os.popen("restart powerd") 
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count1=a.readline()
 print("count1=",count1[:-1])
if count1 > count:
   print('SUCCESS')
   data = ["s0ix_states","S0ix_001","SUCCESS","on powerd_dbus_suspend"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
   print('FAILURE')
   data = ["thermal","thermal_014","FAILURE","DPTF disabled"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
