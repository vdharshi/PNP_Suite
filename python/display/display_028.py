#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_028")
print("Test Case ID display_028: checks whether display frequency = 60")
freq=os.popen("cat /sys/kernel/debug/dri/0/i915_display_info | grep mode | head -1 | cut -f5 -d ' '| tr -d ':'").read()
print(freq)
if freq== '60':
    print('SUCCESS')
    data = ["display","display_028","SUCCESS",f"display frequency is {freq[:-1]}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_028",f"FAILURE",f"display frequency is {freq[:-1]} not 60"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
