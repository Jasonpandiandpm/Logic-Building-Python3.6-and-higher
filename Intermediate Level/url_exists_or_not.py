'''
31.Check whether URL exists in given string or not
'''
import requests
try:
	requests.get("https://google.com/")
	print("Given URL exists")
except:
	print("Given URL Does not exists")