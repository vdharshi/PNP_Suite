
   import Global_Var
   print("Executing PPM_040")
   print("Test Case ID PPM_040: Check PLL OFF STATUS for USB2")
   file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
   string1 ='xDCI1_D3_STS'
   index = 0
   for line in file1:
    index=index+1
    if string1 in line:
      s=line.replace(" ","")
      n=len(s)
      if '1' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""SUCCESS, xDCI1_D3_STS status is OFF")
      elif '0' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""FAILURE,xDCI1_D3_STS STATUS IS ON")
   file1.close()
   