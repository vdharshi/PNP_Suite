#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing mem_004")
print("Test Case ID mem_004: Displays the memory Channel")
r=os.popen("dmidecode -t memory | grep -i channel | awk '{print $2}' | head -1").read()
print(f"Channel is {r[:-1]}")
print("INFORMATIVE")
data = ["Memory","mem_004","INFORMATION",f"Memory Channel is {r[:-1]}"]
with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
