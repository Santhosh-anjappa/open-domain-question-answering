from urllib import request
from bs4 import BeautifulSoup
import requests
import re
def  getArticles(keywords):
	baseurl = 'http://en.wikipedia.org/w/api.php'
	my_atts = {
		'action' : 'query',
		'format' : 'json',
		'list' : 'search',
		'srlimit' : 4	# change to get more number of articles, like fetching 4 articles for each keyword(which r space seperatedbigrams)
	}

	print("Fetching Articles.............")
	link = []
	for i in keywords:
		# print(i)
		my_atts['srsearch'] = i 				# giving search term
		resp = requests.get(baseurl, params=my_atts)
		data = resp.json()
		for i in data['query']['search']:			# getting the list of all links
			link.append("https://en.wikipedia.org/?curid="+str(i['pageid']))	# a bug here title and repeated results
			# print(i['title'], "\t", link)
	count = 0
	for url in link:						# writing articles to files
		print(url)
		html = request.urlopen(url)
		raw = BeautifulSoup(html, 'html.parser')
		# fp = open("doc/"+str(count)+".txt","a",encoding='utf8')
		para = raw.find_all("p")
		fp = open("doc/"+str(count)+".txt","a",encoding='utf8')
		for i in para:
			fp.write(i.get_text()+"\n")			# writing to the file each paragraph in the article
			
		#count1 += 1
		fp.close()
		count+=1
	
	return len(link)						# returning the number of article fetched