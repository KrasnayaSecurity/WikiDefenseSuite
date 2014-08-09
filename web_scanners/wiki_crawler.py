#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import time

######################################
#      CONFIGURATION                 #
######################################
domain = "rationalwiki.org"

#####################################

def web_r(url_frag):
	w_req = requests.get("http://"+ domain +""+ url_frag )
	return w_req

def get_links(response):
	page_links = []
	for a in response.find_all('a'):
		href = a.get('href', '')
		if href.startswith('/wiki'):
			page_links.append(href)
	return page_links

def msanititize(l_list):
	n_list = []
	for link in l_list:
		if link not in n_list:
			n_list.append(link)
	return n_list

req = web_r("/wiki/RationalWiki:Saloon_bar")
res = req.text
res = BeautifulSoup(res)
links = get_links(res)
links = msanititize(links)
print links
all_links = []
all_links.append(links)
runs = 0

for cycle in all_links:
	links = all_links[runs]
	for link in links:
		req = web_r(link)
		res = req.text
		res = BeautifulSoup(res)
		for text in res.find_all("h1"):
			print text.get_text()
		links = get_links(res)
		links = msanititize(links)
		all_links.append(links)
		time.sleep(1)

	#req = web_r(all_links[runs[0]])
	#res = req.text
	#res = BeautifulSoup(res)
	#links = get_links(res)
	#links = msanititize(links)
	#print links
	runs = runs + 1
	time.sleep(1)


