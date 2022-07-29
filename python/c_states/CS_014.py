#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_014: The Platform shall support checking the hardware counter increment")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
x=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={x}")
print(f"value={y}")
print("Please wait display will go off and wake after RTC alarm of 1 minute")
ctr=0
with open("/sys/class/rtc/rtc0/wakealarm",'w') as f:
 x=os.popen("echo `date '+%s' -d '+ 20 seconds'`").read()
 f.write(x)
os.popen("set_power_policy --ac_screen_off_delay=10 --battery_screen_off_delay=10")
time.sleep(30)
x1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={x1}")
print(f"value={y1}")
time.sleep(5)
if x1>x:
 print("SUCCESS: PC8 counter is increasing as expected")
 ctr=ctr + 1 
else:
 print("FAILURE: PC8 counter is not increasing as expected")
if y1>y:
 print("SUCCESS: PC10 counter is increasing as expected")
 ctr=ctr + 1 
else:
 print("FAILURE: PC10 counter is not increasing as expected")

if ctr==2:
 print("SUCCESS")
 data=["c_states","CS_014","SUCCESS","Platform supports checking the hardware counter increment"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_014","FAILURE","Platform doesnot support checking the hardware counter increment"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
