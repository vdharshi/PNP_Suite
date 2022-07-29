#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_020: Platform should enter PC6, PC8 and PC10 C state while display is ON for PSR Panel")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
time.sleep(10)
ctr=0
print("checking new package state PC6, PC8 and PC10 register value now")
v=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C6' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
x=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={v}")
print(f"value={x}")
print(f"value={y}")
time.sleep(60)
print("checking new package state PC6, PC8 and PC10 register value after 1 minute")
v1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C6' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
x1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={v1}")
print(f"value={x1}")
print(f"value={y1}")
time.sleep(5)
if v1>v:
 print("SUCCESS: PC6 counter is increasing as expected")
 ctr=ctr+1
else:
 print("FAILURE: on Checking through MSR: PC6 counter is not increasing as expected")
if x1>x:
 print("SUCCESS: PC8 counter is increasing as expected")
 ctr=ctr+1
else:
 print("FAILURE: on Checking through MSR: PC8 counter is not increasing as expected")
if y1>y:
 print("SUCCESS: PC10 counter is increasing as expected")
 ctr=ctr+1
else:
 print("FAILURE: on Checking through MSR: PC10 counter is not increasing as expected")
if ctr==3:
 print("SUCCESS")
 data=["c_states","CS_020","SUCCESS","PC6 PC8 PC10 are incremneting while display is ON for PSR Panel"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_020","FAILURE","PC6 PC8 PC10 are not incrementing while display is ON for PSR Panel"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
