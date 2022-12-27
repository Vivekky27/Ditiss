#!/usr/bin/python3
import requests, re, sys
#url="http://cdac.in"
r = requests.get(sys.argv[1], timeout=10)
#f = open("reg1.txt","w+")
#s = r.text
#f.writelines(s)
t=re.findall("<title>(.*?)</title>",  r.text)
print(t)

	
