file1=open("title.txt")
file2=open("string.txt")
index1=0
index2=0
r=1
for line in file1 :
  index1=index1+1
  title=line.file1
  for line in file2: 
   index2=index2+1
   string=line.file2
   n=len(string)
   fb=open("PPM_0{}.py".format(r), "w")
   fb.writelines(
   """
   import Global_Var
   print("Executing PPM_0{}")
   print("Test Case ID PPM_0{}: Check {}")
   file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
   string1 ='{}'
   index = 0
   for line in file1:
    index=index+1
    if string1 in line:
      s=line.replace(" ","")
      n=len(s)
      if '1' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""SUCCESS, {} status is OFF")
      elif '0' in s[n-2]:
       print("SUCCESS")
       with open(Global_Var.result_path/'A.csv', 'a'):
	      print("Pch_pm,PPM_001,""FAILURE,{} STATUS IS ON")
   file1.close()
   """
   .format(r,r,title[:v-1],string[:n-1],string[:n-1],string[:n-1]))
   fb.close()
   break  
  r=r+1
  print(r)
if r==67: print("SUCCESS")
 