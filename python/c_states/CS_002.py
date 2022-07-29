#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID CS_002: The platform shall support the CPU core & package states C2 to C6")
cpu_core=Global_Var.max_no_of_cores
ctr=0
actual2=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"PC2:{actual2}")
if int(actual2[:-1]) > 0:
 ctr=ctr+1
actual3=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C3' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"PC3:{actual3}")
if int(actual3[:-1]) > 0:
 ctr=ctr+1
actual4=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C6' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"PC6={actual4}")
if int(actual4[:-1]) > 0:
 ctr=ctr+1
if ctr==3:
  print("SUCCESS")
  data = ["c_states","CS_002","SUCCESS","Platform Supports CPU core & Package C state"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["c_states","CS_002","FAILURE","Platform Doesn't support CPU core & Package C state"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
 
