#!/usr/bin/python3
import Global_Var
import csv
import time
print("Executing PPM_001")
print("Test Case ID PPM_001: Check PLL OFF STATUS for USB2")
time.sleep(5)
file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
string1 ='USB2PLL_OFF_STS'
index = 0
for line in file1:
 index=index+1
 if string1 in line:
  s=line.replace(" ","")
  n=len(s)
  if '1' in s[n-2]:
    print("SUCCESS")
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     data=["Pch_pm,PPM_001,""SUCCESS, USB2PLL_OFF_STS STATUS is OFF"]
     writer=csv.writer(f)
     writer.writerow(data)
     break
  elif '0' in s[n-2]:
    print("FAILURE")
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     data=["Pch_pm,PPM_001,""FAILURE,USB2PLL_OFF_STS STATUS IS ON"]
     writer=csv.writer(f)
     writer.writerow(data)
     break
file1.close()
time.sleep(5)
   
