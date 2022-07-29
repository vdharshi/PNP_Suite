#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_008")
print("Test Case ID display_008: Display DC6 support: Display should enter DC6 state when display is Off")
time.sleep(10)

print("BEFORE DISPLAY OFF: saving the DC6 value in varaible reg_val")
with open("/sys/kernel/debug/dri/0/i915_dmc_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "DC6" in line:
   reg_val=line[-2:-1]
   print("reg_val:",reg_val)
   break
time.sleep(5)

print("RTC alarm wake event set after 2 minutes")
with open ("/sys/class/rtc/rtc0/wakealarm", 'w') as a:
 x=os.popen("date '+%s' -d '+ 60 seconds'").read()
 a.write(x)

print("Turning the display off in 30 seconds if AC connected")
os.popen("set_power_policy --ac_screen_off_delay=10")
time.sleep(1)
print("Turning the display off in 30 seconds if Battery connected")
os.popen("set_power_policy --battery_screen_off_delay=10")
time.sleep(1)

time.sleep(120)

print("DUT woken up by RTC alarm")

print("setting the display off value to default in Ac connected: 8 minutes")
os.popen("set_power_policy --ac_screen_off_delay=480")
time.sleep(1)
print("setting the display off value to default in Battery connected: 6 minutes")
os.popen("set_power_policy --battery_screen_off_delay=360")
time.sleep(1)


print("AFTER DISPLAY OFF: saving the DC6 value in varaible reg_val1")
with open("/sys/kernel/debug/dri/0/i915_dmc_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "DC6" in line:
   reg_val1 = line[-2:-1]
   print("reg_val1:",reg_val1)
   break
  
time.sleep(5)
if reg_val1 > reg_val:
    print('SUCCESS')
    data = ["display","display_007","SUCCESS","Display enters DC6 state when display is Off"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_007","FAILURE","Display is not entering DC6 state when display is Off"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
