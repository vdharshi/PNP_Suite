
   import Global_Var
   print("Executing PPM_024")
   print("Test Case ID PPM_024: Check PG STATUS for LSX")
   file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
   string1 ='LSX_PG_STS'
   index = 0
   for line in file1:
    index=index+1
    if string1 in line:
      s=line.replace(" ","")
      n=len(s)
      if '1' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""SUCCESS, LSX_PG_STS status is OFF")
      elif '0' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""FAILURE,LSX_PG_STS STATUS IS ON")
   file1.close()
   