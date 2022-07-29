#!/usr/bin/python3
import csv
import Global_Var
print("Executing Test Case thermal_008")
print("Test Case ID thermal_008: Information: Reads PL2 Time Window from sysfs")
with open("/sys/class/powercap/intel-rapl/intel-rapl:0/constraint_1_time_window_us", 'r') as f:
 p=f.read()
 print(p[:-1])
 PL2=((int(float(p)))/1000000)
 print(f"PL2 Time Window={PL2}")
 print("INFORMATION")
 with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_008","INFORMATION",f"PL2 Time Window(SYS_FS)={PL2}"]
  writer=csv.writer(a)
  writer.writerow(data)
