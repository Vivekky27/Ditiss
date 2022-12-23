#!/usr/bin/python3
import argparse, os
parser = argparse.ArgumentParser(description="This is test tool")
parser.add_argument("-c", type=str, help="Type command", required=True)

a = parser.parse_args()
domain=(" ","host -t A",a.c)
os.system(domain)
