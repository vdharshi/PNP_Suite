#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing mem_002")
print("Test Case ID mem_002: Displays the memory Size")
r=os.popen("dmidecode -t memory | grep -i size | awk '{print $2}' | head -1").read()
print("Size is ",r[:-1],"MB")
print("INFORMATIVE")
data = ["Memory","mem_002","INFORMATION",f"Memory Size is {r[:-1]} MB"]
with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
