#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing Test Case: thermal_017")
print("thermal_017,Displays temprature of Thermal zones")
APP_FOLDER = '/sys/class/thermal'
totalDir = 0
i=0
for base, dirs, files in os.walk(APP_FOLDER):
    for directories in dirs:
     if 'thermal' in directories:
        totalDir =totalDir+1
  
ty=[]
print('Total zones are',totalDir)
while i<totalDir:
 with open (f'/sys/class/thermal/thermal_zone{i}/temp', 'r') as f:
  p=f.readline()
  ty.append(p[:-1])
 i=i+1
print(ty)
if totalDir!= 0:
   print('SUCCESS')
   data = ["thermal","thermal_017","SUCCESS",f"Tempratures of {totalDir} zones are {ty}"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
   print('FAILURE')
   data = ["thermal","thermal_017","FAILURE","unable to find sysfs entry"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
