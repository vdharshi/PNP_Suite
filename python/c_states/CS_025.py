#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_025: The platform shall support new package state PC2 for Idle Display ON Usecase")
print("checking new package state PC2 value")
x=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={x}")
time.sleep(60)
print("checking new package state PC2 register value after a minute delay")
val1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={val1}")
if val1>x:
 print("SUCCESS on new package state PC2 for Idle Display ON Usecase incrementation")
 data=["c_states","CS_025","SUCCESS","Package state PC2 for IDO gets incremented"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_025","FAILURE","Package state PC2 for IDO Usecase doesn't gets incremeneted"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
