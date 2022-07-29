#1/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID perf_001: coreboot boot up time for warm boot should meet google's requirement of 1 seconds")
cb_boot_time=os.popen("cbmem -T | tail -1 | awk '{print $2}'").read()
cb_boot_time=(int(cb_boot_time))/1000
print(f"cb_boot_time: {cb_boot_time}")
if cb_boot_time <= 1000:
  print("SUCCESS")
  data = ["performance","perf_001","SUCCESS",f"cb_boot_time: {cb_boot_time}; coreboot boot up time for warm boot meets google's requirement of 1 seconds"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data=["performance","perf_001","FAILURE",f"cb_boot_time: {cb_boot_time}; coreboot boot up time for warm boot is not meeting google's requirement of 1 seconds"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)