#!/usr/bin/python3
import csv
import Global_Var
print("Executing Test Case: thermal_012")
print("thermal_012,checking whether fan or fanless")
index=0
flag=0
r=0
string1='TFN'
while r<2:
 with open(f"/sys/class/thermal/cooling_device{r}/type", 'r') as f:
  for line in f:  
     index=index+1 
     if string1 in line:
       flag = 1
       break
 r=r+1
 
if flag == 0: 
   print('FAILURE')
   data = ["thermal","thermal_012","FAILURE","Fanless Platform"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    # write the data
    writer.writerow(data) 
else: 
   print('SUCCESS')
   data = ["thermal","thermal_012","SUCCESS","Platform has Fan"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
