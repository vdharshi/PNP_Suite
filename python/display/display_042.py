#!/usr/bin/python3
import os
import csv
import sys
import time
import Global_Var
print("Test Case ID display_042: Display DC5 support: Display should enter DC5 state when display is Off")
time.sleep(10)
print("BEFORE DISPLAY OFF: saving the DC5 value in varaible reg_val")
reg_val=os.popen("cat /sys/kernel/debug/dri/0/i915_dmc_info | grep 'DC5 count' | cut -d ':' -f2 | tr -d ' '").read()
print("reg_val:"+reg_val)
time.sleep(5)
print("RTC alarm wake event set after 2 minutes")
with open("/sys/class/rtc/rtc0/wakealarm",'w')as f:
 d=os.popen("date '+%s' -d '+ 2 minute'").read()
 f.write(d)
print("Turning the display off in 30 seconds if AC connected")
os.system("set_power_policy --ac_screen_off_delay=10")
time.sleep(1)

time.sleep(120)
print("DUT woken up by RTC alarm")
print("setting the display off value to default in Ac connected: 8 minutes")
os.system("set_power_policy --ac_screen_off_delay=480")
time.sleep(1)
print("setting the display off value to default in Battery connected: 6 minutes")
os.system("set_power_policy --battery_screen_off_delay=360")
time.sleep(1)

print("AFTER DISPLAY OFF: saving the DC6 value in varaible reg_val1")
reg_val1=os.popen("cat /sys/kernel/debug/dri/0/i915_dmc_info | grep 'DC5 count' | cut -d ':' -f2 | tr -d ' '").read()
print("reg_val1:"+reg_val1)
time.sleep(5)

if reg_val1[:-1] >reg_val[:-1]:
  print("SUCCESS")
  data = ["display","display_041","SUCCESS","Display enters DC5 state when display is Off"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data = ["display","display_041","FAILURE","Display is not entering DC5 state when display is Off"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 