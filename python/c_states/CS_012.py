#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_012: The platform shall support checking  whether C-state counters increases after S0ix transition")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
ctr=0
flag=0
print("checking new package state PC8 and PC10 register value before the S0ix")
x=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={x}")
print(f"value={y}")
print("reading the counter before S0ix through powerd_dbus_suspend command")
count=os.popen("cat /sys/kernel/debug/pmc_core/slp_s0_residency_usec").read()
print(count)
with open("/var/lib/power_manager/suspend_to_idle",'w')as f:
 f.write('1')
os.popen("restart powerd")
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
print("reading the counter after S0ix through powerd_dbus_suspend command")
count1=os.popen("cat /sys/kernel/debug/pmc_core/slp_s0_residency_usec").read()
print(count1)
print("checking new package state PC8 and PC10 register value after the S0ix")
x1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={x1}")
print(f"value={y1}")
if count1>count:
 if x1>x:
  print("SUCCESS: PC8 counter is increasing as expected")
  ctr=ctr+1
 else:
  print("FAILURE: PC8 counter is not increasing as expected")
 if y1>y:
  print("SUCCESS: PC10 counter is increasing as expected")
  ctr=ctr+1
 else:
  print("FAILURE: PC10 counter is not increasing as expected")
else:
 flag=1
 print("CS_012, S0ix is not happening")
if flag ==1:
 data = ["c_states","CS_012","FAILURE","S0ix not happening; so checking PC8 PC10 during s0ix is invalid"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
elif ctr==2:
 data = ["c_states","CS_012","SUCCESS","PC8 PC10 are incrementing after S0ix transition"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 data = ["c_states","CS_012","FAILURE","PC8 PC10 are not incrementing after S0ix transition"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)  
