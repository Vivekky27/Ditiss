#!/usr/bin/python3
import sys,os
def func():
	if sys.argv[1]== '-c':
		os.system(sys.argv[2])
	elif sys.argv[1]== '-h':
		print("-h for help")
	else:
		print("error")
func()
