#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_010: Verify whether platform support checking the C-state counters while running CPU intensive workload")

os.popen("//home/OSPM-Test-Suite/functionality_test_cases/config/stress -c 4 -t 100 &")
time.sleep(10)
count1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"count1:{count1}")
time.sleep(60)
count2=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"count2={count2}")
if count2 > count1:
 print("SUCCESS")
 data=["c_states","CS_010","SUCCESS",f"PC2_count2:{count2};PC2_count1:{count1} platform support checking the C-state counters while running CPU intensive workload"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_010","FAILURE",f"PC2_count2:{count2};PC2_count1:{count1} platform doesnot support checking the C-state counters while running CPU intensive workload"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
