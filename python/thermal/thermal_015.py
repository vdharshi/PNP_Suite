#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing Test Case: thermal_015")
print("thermal_015,Displays the total number and name of Thermal sensors")
y = os.popen("ectool tempsinfo all | wc -l").read()
x = os.popen("ectool tempsinfo all").read()
a=[]
with open(Global_Var.result_path/'B.txt', 'w') as file1:
 file1.write(x)
with open(Global_Var.result_path/'B.txt', 'r')as file1:
 index=0
 for line in file1:
   index=index+1
   s=line.replace(" ","")
   n=len(s)
   a.append(s[3:n-1])
   
if y != '0':
    print('SUCCESS')
    print(a)
    data = ["thermal","thermal_015","SUCCESS",f"Total {y[:-1]} Thermal sensors namely {a}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["thermal","thermal_015","FAILURE","unable to find ectool tempsinfo all sysfs entry"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
    writer.writerow(data) 
