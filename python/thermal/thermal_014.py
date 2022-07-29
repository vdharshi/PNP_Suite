#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing Test Case: thermal_014")
print("thermal_014,checking whether DPTF is enabled")
x = os.popen("status dptf").read()
x.replace(" ","")
s=x[5:10]

if s == 'start':
   print('SUCCESS')
   data = ["thermal","thermal_014","SUCCESS","DPTF enabled"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
   print('FAILURE')
   data = ["thermal","thermal_014","FAILURE","DPTF disabled"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
