#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time

#################################
#       Configuration           #
#################################
domain = "en.wikipedia.org"
delay = 600

#################################

page = raw_input("Enter the full name of the page that you want to monitor: ")

def makeURL(title):
	encoded = title.replace(" ","_")
	return encoded

page = makeURL(page)

def saloonBarReq():
	reqData = {"action" : "raw"}
	reqHeaders = {"User-Agent":"WMF talk page scanner: Sokolovskaya, Checking WMF talk pages for evidence of harassment and foul play, sokolovskaya.akula.sturmkrieg.ru in Dallas, Texas"}
	req = requests.post("http://"+ domain +"/wiki/"+ page, data=reqData, headers=reqHeaders)
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

wordList = ["the", "is", "soviet", "khan", "nazi"]

while True:
	t = time.localtime()
	timestamp = "\n"+ time.asctime(t)
	print timestamp
	file = open(""+ domain +"-"+ page +"_log.txt", 'a')
	text = "\n\n"+ timestamp +"\n"+ req +"\n\n"
	file.write(text)
	file.close()
	for word in wordList:
		i = 0
		check = checkWord(word)
		if ( check == True ):
			file = open(""+ domain +"-"+ page +"_log.txt", 'a')
			text = word.upper() +": TRUE "+ str(count[i]) +"\n"
			file.write(text)
			file.close()
		else:
			file = open(""+ domain +"-"+ page +"_log.txt", 'a')
			text = word.upper() +": FALSE\n"
			file.write(text)
			file.close()
		i = i + 1
	time.sleep(delay)

