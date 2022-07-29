#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_027: Verify whether the platform supports c state residency in the pmc driver")
c_arr=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | awk '{print $4}'").read()
c_var=0
no_var=0
for x in c_arr:
 if x != 0:
  c_var=c_var+1
 else:
  no_var=no_var+1

if no_var!=0:
 print("FAILURE")
 data = ["c_states","CS_027","FAILURE","Device doesnt support c_state residencies in pmc driver"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("SUCCESS")
 data=["c_states","CS_027","SUCCESS","Device supports c_state residencies in the pmc driver"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
