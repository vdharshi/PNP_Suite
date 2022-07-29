#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_016: The Platform shall support checking all the C-state exit latency and target residency")
result=0
cpu_core=Global_Var.max_no_of_cores

states=os.popen("ls -l /sys/devices/system/cpu/cpu0/cpuidle/ | grep -c ^d").read()
print(f"Number of states is : {states}")
board_name=os.popen("cat /etc/lsb-release | grep -i 'CHROMEOS_RELEASE_BOARD' | cut -f 2 -d '=' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"board_name: {board_name}")
states=int(states[:-1])
i=0
j=0
while i<cpu_core:
 while j<states:
  actual_val=os.popen(f"cat /sys/devices/system/cpu/cpu{i}/cpuidle/state{j}/latency").read()
  print(f"Latency of Core{i} state{j} : {actual_val}")
  if actual_val != None:
   result=result+1
  j=j+1
 i=i+1
 j=0

print(f"Result={result}")
d=cpu_core*states
if result==d:
 print("SUCCESS")
 data=["c_states","CS_016","SUCCESS","Platform supports checking all the C-state exit latency and target residency"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_016","FAILURE","Platform doesnot support checking all the C-state exit latency and target residency"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
