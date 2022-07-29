#!/usr/bin/python3
import csv
import Global_Var
print("Executing Test Case thermal_007")
print("Test Case ID thermal_007: Information: Reads PL1 Time Window from sysfs")
with open("/sys/class/powercap/intel-rapl/intel-rapl:0/constraint_0_time_window_us", 'r') as f:
 p=f.read()
 print(p[:-1])
 PL1=((int(float(p)))/100000)
 print(f"PL1 Time Window={PL1}")
 print("INFORMATION") 
with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_007","INFORMATION",f"PL1 Time Window(SYS_FS)={PL1}"]
  writer=csv.writer(a)
  writer.writerow(data)
