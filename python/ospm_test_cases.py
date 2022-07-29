#!/usr/bin/python3
import os
import sys
from xml.dom import minidom
import subprocess

def help():
	print ("")
	print ("USAGE: python ospm_test_cases.py <argv 1> <argv 2> <argv 3> ... <argv n>")
	print ("")
	print ("----------------------------------------------------------------------------------------------------------")
	print ("Arguments		-	Definitions				 ")
	print ("----------------------------------------------------------------------------------------------------------")
	print ("chrome_ospm		-	Runs all the Component of test suite listed in /home/python/selective.xml")
	print ("c_states		-	Runs all C-state test cases")
	print ("p_states		-	Runs all P-state test cases")
	print ("s0ix_states		-	Runs all S0ix-state test cases")
	print ("graphics		-	Runs all Graphics test cases")
	print ("display			-	Runs all Display test cases")
	print ("thermal			-	Runs all Thermal test cases")
	print ("device_pm		-	Runs all Device-PM test cases")
	print ("kernel_pm		-	Runs all Kernel-PM test cases")
	print ("cpu_hotplug		-	Runs all CPU-HotPlug test cases")
	print ("performance		-	Runs all Performence test cases")
	print ("memory                  -       Runs all Memory test cases")
	print ("pch_pm			-	Runs all PCH_PM test cases")
	print ("---------------------------------------------------------------------------------------------------------")


def c_states():
	print("inside func")
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('cstate')
	for s in itemlist :
		print("SCRIPT NAME : ", s.firstChild.nodeValue)
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def p_states():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('pstate')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def s0ix_states():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('s0ix')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def graphics():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('graphics')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def display():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('display')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		if "py" in actual_path:
			actual_path = "python3 "+actual_path
			os.system(actual_path)
		else:
			subprocess.call(actual_path)

def thermal():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('thermal')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path, shell=True)

def device_pm():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('device')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def kernel_pm():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('kernel')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def cpu_hotplug():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('cpu')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def performance():
	xmldoc = minidom.parse('/home/python/selective.xml')
	itemlist = xmldoc.getElementsByTagName('perf')
	for s in itemlist :
		#print "SCRIPT NAME : ", s.firstChild.nodeValue
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)
def memory():
	xmldoc = minidom.parse("/home/python/selective.xml")
	itemlist = xmldoc.getElementsByTagName('mem')
	for s in itemlist :
		path1=s.firstChild.nodeValue
		actual_path=path1.rstrip()
		subprocess.call(actual_path)

def pch_pm():
        xmldoc = minidom.parse("/home/python/selective.xml")
        itemlist = xmldoc.getElementsByTagName('pch')
        for s in itemlist :
                path1=s.firstChild.nodeValue
                actual_path=path1.rstrip()
                subprocess.call(actual_path,shell=True)

path="/home/python"
if os.path.exists(path):
	for number in range(len(sys.argv)):
		if len(sys.argv) < 2 or sys.argv[number] == "--help" or sys.argv[number] == "-h":
			help();
			sys.exit()
		elif sys.argv[number] == sys.argv[0]:
			continue
		elif sys.argv[number] == "chrome_ospm":
			c_states();
			p_states();
			s0ix_states();
			graphics();
			display();
			thermal();
			device_pm();
			kernel_pm();
			cpu_hotplug();
			performance();
			memory();
			pch_pm();
		elif sys.argv[number] == "c_states":
			c_states();
		elif sys.argv[number] == "p_states":
			p_states();
		elif sys.argv[number] == "s0ix_states":
			s0ix_states();
		elif sys.argv[number] == "graphics":
			graphics();
		elif sys.argv[number] == "display":
			display();
		elif sys.argv[number] == "thermal":
			thermal();
		elif sys.argv[number] == "device_pm":
			device_pm();
		elif sys.argv[number] == "kernel_pm":
			kernel_pm();
		elif sys.argv[number] == "cpu_hotplug":
			cpu_hotplug();
		elif sys.argv[number] == "performance":
			performance();
		elif sys.argv[number] == "memory":
			memory();
		elif sys.argv[number] == "pch_pm":
                        pch_pm();
		else:
			print("ERROR:	llegal Argument has been passed")
else:
	print("ERROR:	Please copy the OSPM Test Suite into /home/ directory")
