#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time

######################################
#      CONFIGURATION                 #
######################################
domain = "rationalwiki.org"
entry = "RationalWiki:Saloon_bar"
search_terms = ["nazi","ehrenstein","rape","arcane","dondrekhan"]
require = ""
exclude = "archive"

#####################################

def web_r(url_frag):
	reqHeaders = {"User-Agent":"AKULA SOKOLOVSKAYA: sokolovskaya.akula.sturmkrieg.ru"}
	w_req = requests.get("http://"+ domain +""+ url_frag +"", headers=reqHeaders )
	return w_req

def get_links(response):
	page_links = []
	for a in response.find_all('a'):
		href = a.get('href', '')
		if href.startswith('/wiki') and exclude.lower() not in href.lower() and require.lower() in href.lower():
			page_links.append(href)
	return page_links

def msanititize(l_list):
	n_list = []
	for link in l_list:
		if link not in n_list:
			n_list.append(link)
	return n_list

req = web_r("/wiki/"+ entry)
res = req.text
res = BeautifulSoup(res)
links = get_links(res)
links = msanititize(links)
#print links
all_links = []
all_links.append(links)
alert_count = [0] * len(search_terms)
hasAlert = False
runs = 0

for cycle in all_links:
	links = all_links[runs]
	for link in links:
		req = web_r(link)
		res = req.text
		res = BeautifulSoup(res)
		for text in res.find_all("h1"):
			print "\n----------------------------------------------------------------------"+ text.get_text()
		links = get_links(res)
		links = msanititize(links)
		all_links.append(links)
		for text in res.find_all(id="content"):
			print ""+ text.get_text() +"\n"
		for text in res.find_all(['p', "li", "span", "div"]):
			for term in search_terms:
				if term.lower() in text.get_text().lower():
					alert_count[search_terms.index(term)] = alert_count[search_terms.index(term)] + 1
		file = open("WikiCrawl_log.txt", 'a')
		file.write("\n\n"+ link +"\n")
		for term in search_terms:
			print ""+ term +" count = "+ str(alert_count[search_terms.index(term)])
			file.write(""+ term +" count = "+ str(alert_count[search_terms.index(term)]) +"\n")
		for text in res.find_all('p'):
			for term in search_terms:
				if term.lower() in text.get_text().lower():
					hasAlert = True
		if hasAlert == True:
			alert_r = web_r(link +"?action=raw")
			alert_r = alert_r.content
			file.write(""+ alert_r +"\n")
		file.close()
		for i in alert_count:
			alert_count[alert_count.index(i)] = 0
		hasAlert = False
		time.sleep(1)
	runs = runs + 1
	time.sleep(1)


