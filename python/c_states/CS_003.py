#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
reg_1=0
print("Test Case ID CS_003: The platform shall support the applicable CPU package states PC8, PC10")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
print("checking new package state PC2 register value before the display off")
x=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"valuePC8={x}")
print(f"valuePC10={y}")
print("Please wait display will go off and wake after RTC alarm of 1 minute")
with open("/sys/class/rtc/rtc0/wakealarm",'w')as f:
 x=os.popen("date '+%s' -d '+ 20 seconds'").read()
 f.write(x)
os.popen("set_power_policy --ac_screen_off_delay=10 --battery_screen_off_delay=10") 
time.sleep(30)
print("checking new package state PC2 register value after the display off")
x1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C8' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
y1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C10' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"valuePC8={x1}")
print(f"valuePC10={y1}")
if x1>x:
 print("Checking PC8 counter is increasing as expected")
 reg_1=reg_1 + 1
else:
 print("Checking PC8 counter is not increasing as expected")
if y1>y:
 print("Checking PC10 counter is increasing as expected")
 reg_1=reg_1 + 1
else:
 print("Checking PC10 counter is not increasing as expected")
if reg_1 ==2:
 print("SUCCESS")
 data = ["c_states","CS_003","SUCCESS","PC8 PC10 counter is Incrementing after display off"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_003","FAILURE","PC8 PC10 counter are not Incrementing after display off"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
