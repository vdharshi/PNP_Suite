#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing Test Case thermal_011")
print("Test Case ID thermal_011: Information: Reads Battery Energy")
x = os.popen("power_supply_info").read()

with open(Global_Var.result_path/'A.txt', 'r+') as file1:
 file1.write(x)
 index=0
 string1='energy'
 for line in file1:
  index=index+1
  if string1 in line:
   s=line.replace(" ","")
   print(f"Battery energy is {s[-7:-1]} Wh")
   print("INFORMATION")
   with open(Global_Var.result_path/'A.csv', 'a') as a:
     data=["thermal","thermal_011","INFORMATION",f"Battery energy is {s[-7:-1]} Wh"]
     writer=csv.writer(a)
     writer.writerow(data)
   break

