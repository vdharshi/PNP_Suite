#'created by premanand radhakrishnan 19/08/2015 2:18:00
#'vesion : 1.0
#' this file will get the register value, convert into binary value and append it to csv file

import os, sys, csv, subprocess
import time
sleep = time.sleep
from subprocess import Popen, PIPE
def regval(x):
    p = subprocess.Popen(h, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        #print line
        reg = line.strip()
        val = line
        val = line.split('x')
        val = val[1]
        #print val
        #sleep(1)
        #retval = p.wait
        #binary = bin(int(val, 16))[2:]
        binary = bin(int('1'+val, 16))[3:]
        #print binary
        bin1 = str(binary)
        #for i in range (0,len(bin1)):
            #print bin1[i]
        #sleep(1)
        return reg,bin1

def creating_csv(p,q,t,u,c,d,e,f,g,x,y,j,k,l,m,n):
    b = open('regval.csv', 'wb')
    a = csv.writer(b)
    data = [[' ','AGENT ID','EXPECTED STATUS','PMC STATUS REGISTER','REGISTER ADDRESS','FAB3 READ VALUE','FAB3 CURRENT STATUS'],
            ['POWER GATED IP BLOCK', ' ', '0=PFET ON', ' ', ' ', ' ', '0=PFET ON'],\
            [' ', ' ', '1=PFET OFF', ' ', ' ', ' ', '1=PFET OFF'],\
            ['PMC', '0', '1', 'pch.pmc.xram.hr_pfear0a','0xfe000590',p,q[7]],\
            ['OPI_DMI','1','1',' ',' ',' ',q[6]],\
            ['SPI/eSPI','2','1',' ',' ',' ',q[5]],\
            ['XHCI','3','1',' ',' ',' ',q[4]],\
            ['SPA','4','1',' ',' ',' ',q[3]],\
            ['SPB','5','1',' ',' ',' ',q[2]],\
            ['SPC','6','1',' ',' ',' ',q[1]],\
            ['GBE','7','1',' ',' ',' ',q[0]],\
            ['SATA','8','1','pch.pmc.xram.hr_pfear0b','0xfe000591',t,u[7]],\
            ['HDA_PGD0','9','1',' ',' ',' ',u[6]],\
            ['HDA_PGD1','10','1',' ',' ',' ',u[5]],\
            ['HDA_PGD2','11','1',' ',' ',' ',u[4]],\
            ['HDA_PGD3','12','1',' ',' ',' ',u[3]],\
            ['RSVD','13','1',' ',' ',' ',u[2]],\
            ['LPSS','14','1',' ',' ',' ',u[1]],\
            ['LPC','15','1',' ',' ',' ',u[0]],\
            ['SMB','16','1','pch.pmc.xram.hr_pfear0c','0xfe000592',c,d[7]],\
            ['ISH','17','1',' ',' ',' ',d[6]],\
            ['PS2B','18','1',' ',' ',' ',d[5]],\
            ['DFx','19','1',' ',' ',' ',d[4]],\
            ['SCC','20','1',' ',' ',' ',d[3]],\
            ['Reserved','21','1',' ',' ',' ',d[2]],\
            ['Fuse','22','Not supported',' ',' ',' ',d[1]],\
            ['Camera','23','1',' ',' ',' ',d[0]],\
            ['Reserved','24','1','pch.pmc.xram.hr_pfear0d','0xfe000593',e,f[7]],\
            ['USB3_OTG','25','1',' ',' ',' ',f[6]],\
            ['EXI','26','1',' ',' ',' ',f[5]],\
            ['CSE','27','1',' ',' ',' ',f[4]],\
            ['csme_kvm','28','1',' ',' ',' ',f[3]],\
            ['csme_pmt','29','1',' ',' ',' ',f[2]],\
            ['csme_clink','30','1',' ',' ',' ',f[1]],\
            ['csme_ptio','31','1',' ',' ',' ',f[0]],\
            ['csme_usbr','32','1','pch.pmc.xram.hr_pfear1a','0xfe000594',g,x[7]],\
            ['csme_susram','33','1',' ',' ',' ',x[6]],\
            ['csme_smt','34','1',' ',' ',' ',x[5]],\
            ['Reserved','35','1',' ',' ',' ',x[4]],\
            ['csme_sms2','36','1',' ',' ',' ',x[3]],\
            ['csme_sms1','37','1',' ',' ',' ',x[2]],\
            ['csme_rtc','38','1',' ',' ',' ',x[1]],\
            ['csme_psf','39','1',' ',' ',' ',x[0]],\
            ['SBR0','40','1','pch.pmc.xram.hr_pfear1b','0xfe000595',y,j[7]],\
            ['SBR1','41','1',' ',' ',' ',j[6]],\
            ['SBR2','42','1',' ',' ',' ',j[5]],\
            ['SBR3','43','1',' ',' ',' ',j[4]],\
            ['SBR4','44','1',' ',' ',' ',j[3]],\
            ['SBR5','45','1',' ',' ',' ',j[2]],\
            ['Reserved','46','1',' ',' ',' ',j[1]],\
            ['PSF1','47','1',' ',' ',' ',j[0]],\
            ['PSF2','48','1','pch.pmc.xram.hr_pfear1c','0xfe000596',k,l[7]],\
            ['PSF3','49','1',' ',' ',' ',l[6]],\
            ['PSF4','50','1',' ',' ',' ',l[5]],\
            ['Reserved','51','1',' ',' ',' ',l[4]],\
            ['Reserved','52','1',' ',' ',' ',l[3]],\
            ['Reserved','53','1',' ',' ',' ',l[2]],\
            ['Reserved','54','1',' ',' ',' ',l[1]],\
            ['Reserved','55','1',' ',' ',' ',l[0]],\
            ['Reserved','56','1','pch.pmc.xram.hr_pfear1d','0xfe000597',m,n[7]],\
            ['Reserved','57','1',' ',' ',' ',n[6]],\
            ['Reserved','58','1',' ',' ',' ',n[5]],\
            ['Reserved','59','1',' ',' ',' ',n[4]],\
            ['Reserved','60','1',' ',' ',' ',n[3]],\
            ['Reserved','61','1',' ',' ',' ',n[2]],\
            ['Reserved','62','1',' ',' ',' ',n[1]],\
            ['Reserved','63','1',' ',' ',' ',n[0]]]

    a.writerows(data)
    b.close()

for i in range(0,8):

    h = "iotools mmio_read8 0xfe00059"+str(i)
    sleep(1)
    if (h == "iotools mmio_read8 0xfe000590"):
        p,q = regval(h)
        print "regval:",p+" bin:",q       
        #creating_csv(p,q)
        #return p,q
        pass
    elif (h == "iotools mmio_read8 0xfe000591"):
        t,u = regval(h)
        print "regval:",t+" bin:",u
        #print t,u
        #creating_csv(a,b)
        #return a,b
        pass
    elif (h == "iotools mmio_read8 0xfe000592"):
        c,d = regval(h)
        print "regval:",c+" bin:",d 
        #print c,d
        #creating_csv(c,d)
        #return c,d
        pass
    elif (h == "iotools mmio_read8 0xfe000593"):
        e,f = regval(h)
        print "regval:",e+" bin:",f 
        #print e,f
        #creating_csv(e,f)
        #return e,f
        pass
    elif (h == "iotools mmio_read8 0xfe000594"):
        g,x = regval(h)
        print "regval:",g+" bin:",x 
        #print g,x
        #return g,x
        #creating_csv(g,x)
        pass
    elif (h == "iotools mmio_read8 0xfe000595"):
        y,j = regval(h)
        print "regval:",y+" bin:",j 
        #print y,j
        #return i,j
        #creating_csv(j,q)
        pass
    elif (h == "iotools mmio_read8 0xfe000596"):
        k,l = regval(h)
        print "regval:",k+" bin:",l 
        #print k,l
        #creating_csv(k,l)
        #return k,l
        pass
    elif (h == "iotools mmio_read8 0xfe000597"):
        m,n = regval(h)
        print "regval:",m+" bin:",n 
        #print m,n
        #return m,n
        #creating_csv(m,n)
        pass
    else:
        print 'unknown register'
        pass

creating_csv(p,q,t,u,c,d,e,f,g,x,y,j,k,l,m,n)

    
 




