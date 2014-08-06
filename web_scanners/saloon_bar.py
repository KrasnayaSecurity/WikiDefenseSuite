#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import datetime
 
def saloonBarReq():
	reqData = {"action" : "raw"}
	reqHeaders = {"User-Agent":"Saloon Bar scanner: Sokolovskaya, Checking Rational Wiki Saloon Bar for evidence of harassment, sokolovskaya.akula.sturmkrieg.ru in Dallas, Texas"}
	req = requests.post("http://rationalwiki.org/wiki/RationalWiki:Saloon_bar", data=reqData, headers=reqHeaders)
	req.encoding = "utf-8"
	return req.content
 
req = saloonBarReq()
 
def checkWord(word):
	if ( word in req.lower() ):
		print word.upper() +": TRUE"
		return True
	else:
		print word.upper() +": FALSE"
		return False
 
wordList = ["ehrenstein", " ie ", "inquisitor", "sasha", "lieutenant s", "reznov", "dondrekhan", "dewey", "nazi", "rape"]
 
while True:
	t = time.localtime()
	timestamp = "\n"+ time.asctime(t)
	print timestamp
	file = open("saloonbar_log.txt", 'a')
	text = "\n\n"+ timestamp +"\n"+ req +""
	file.write(text)
	file.close()
	for word in wordList:
		check = checkWord(word)
		if ( check == True ):
			file = open("saloonbar_log.txt", 'a')
			text = word.upper() +": TRUE\n"
			file.write(text)
			file.close()
		else:
			file = open("saloonbar_log.txt", 'a')
			text = word.upper() +": FALSE\n"
			file.write(text)
			file.close()
	time.sleep(600)