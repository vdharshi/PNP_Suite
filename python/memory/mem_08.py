import os
import csv
import Global_Var
import time
print("Executing mem_008")
print("Test Case 008: eMMC resume and display suspend resume should be async")
x=os.popen("cat /sys/bus/pci/devices/0000\:00\:02\.0/power/async").read()

x=x[:-1]
if x=='0':
 data = ["Memory","mem_08","FAILURE","unable to find async sysfs entry" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
elif x == 'enabled':
 data = ["Memory","mem_08","SUCCESS","eMMC resume and display suspend resume are async" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
 data = ["Memory","mem_08","FAILURE","eMMC resume and display suspend are not async" ]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
