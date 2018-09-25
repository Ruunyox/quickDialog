#! /usr/local/bin/python3

from sys import platform
from os import popen, listdir, path

if platform in ("darwin","linux","linux2"):
	try:
		from dialog import Dialog
		dlg = Dialog(dialog='dialog')
		rows, cols = popen('stty size','r').read().split()
		rows= int(rows)
		cols= int(cols)
	except:
		print("Error: PyDialog and/or dialog backend not found.")
		print("Run \"dialog --version\" and/or \"pip list | grep dialogi\".")
		print("Aborting script...")
		exit()

def fs(rows,cols):
	files = [(f,f,0) for i,f in enumerate(listdir('.')) if path.isfile(f)]
	code, choose = dlg.buildlist("Select File(s)",int(3*rows/4),int(3*cols/4),int(3*rows/4)-4,items=files)
	if code == Dialog.OK:
		return choose
	else:
		return None

def __main__():
	f = fs(rows,cols)

__main__()

