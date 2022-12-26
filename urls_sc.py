#!/usr/bin/python3
import requests
url = open("url.txt" , "r+")
for i in url.readlines():
	print(i)
	f = i.strip("\n")
	print(f)
	r = requests.get(f ,timeout=10)
	print(r.status_code)




