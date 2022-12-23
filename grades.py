#!/usr/bin/python3
import sys

#function	
def compute_grade():
		x=float(sys.argv[1])
		if x >= 1.0:
			print("Invalid")
		elif x >= 0.9:
			print("A grade")
		elif x >= 0.8:
			print("B grade")
		elif x >= 0.7:
			print("C grade")
		elif x >= 0.6:
			print("D grade")
		elif x > 0.0 and x < 0.6:
			print("F grade")


compute_grade()
