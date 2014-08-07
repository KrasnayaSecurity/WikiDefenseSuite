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
count = [0] * 20

def checkWord(word):
	i=0
	if ( word in req.lower() ):
		occr = req.lower().count(word)
		print word.upper() +": TRUE "+ str(occr)
		count[i] = occr
		return True
	else:
		print word.upper() +": FALSE"
		return False
	i = i + 1

wordList = ["ehrenstein", " ie ", "inquisitor", "sasha", "the", "lieutenant s", "reznov", "dondrekhan", "dewey", "nazi", "rape", "arcane", "arcane21"]

while True:
	t = time.localtime()
	timestamp = "\n"+ time.asctime(t)
	print timestamp
	file = open("saloonbar_log.txt", 'a')
	text = "\n\n"+ timestamp +"\n"+ req +"\n\n"
	file.write(text)
	file.close()
	for word in wordList:
		i = 0
		check = checkWord(word)
		if ( check == True ):
			file = open("saloonbar_log.txt", 'a')
			text = word.upper() +": TRUE "+ str(count[i]) +"\n"
			file.write(text)
			file.close()
		else:
			file = open("saloonbar_log.txt", 'a')
			text = word.upper() +": FALSE\n"
			file.write(text)
			file.close()
		i = i + 1
	time.sleep(600)

