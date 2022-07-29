#!/usr/bin/python3
import csv
import Global_Var
print("Executing Test Case: thermal_013")
print("thermal_013,checking whether RAPL is enabled")
with open("/sys/class/powercap/intel-rapl/enabled", 'r') as f:
 r=f.read()
if '1' in r[0]:
 print("SUCCESS")
 data=["thermal","thermal_013","SUCCESS","RAPL enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
else:
 print("FAILURE")
 data=["thermal","thermal_013","FAILURE","RAPL disabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
