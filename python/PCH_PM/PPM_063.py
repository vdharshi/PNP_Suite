
   import Global_Var
   print("Executing PPM_063")
   print("Test Case ID PPM_063: Check PLL OFF STATUS for USB2")
   file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
   string1 ='SMLINK1_VNN_REQ_STS'
   index = 0
   for line in file1:
    index=index+1
    if string1 in line:
      s=line.replace(" ","")
      n=len(s)
      if '1' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""SUCCESS, SMLINK1_VNN_REQ_STS status is OFF")
      elif '0' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""FAILURE,SMLINK1_VNN_REQ_STS STATUS IS ON")
   file1.close()
   