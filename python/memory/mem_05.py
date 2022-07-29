import os
import csv
import Global_Var
import time
print("Executing mem_005")
print("Test Case ID mem_005: Displays the memory Bits")
r=os.popen("dmidecode -t memory | grep -i Data | tail -1 | awk '{print $3}'").read()
print(f"{r[:-1]} Bits")
print("INFORMATIVE")
data = ["Memory","mem_005","INFORMATION",f"Memory is {r[:-1]} bits"]
with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)