#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_007: Verify whether the platform support checking the cpu idle counters PC8 after an S0ix iteration")
with open("/var/lib/power_manager/suspend_to_idle",'w')as f:
 f.write('1')
os.popen("restart powerd")
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
count1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"count1:{count1}")
time.sleep(60)
count2=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"count2:{count2}")
if count2 > count1:
 print("SUCCESS")
 data=["c_states","CS_007","SUCCESS",f"PC8_count2:{count2};PC8_count1:{count1} platform support checking the cpu idle counters after an S0ix iteration"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_007","FAILURE",f"PC8_count2:{count2};PC8_count1:{count1} platform does not support checking the cpu idle counters after an S0ix iteration"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
