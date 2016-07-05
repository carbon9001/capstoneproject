#this file is for crawling game info from the store_page with game id
#what we try to have:
#game mode
#game genre 
#user define game genre(probably not)
#release date

#<td class="span3">Genres</td>
#<td>Action,Adventure,Massively Multiplayer,Simulation,Early Access</td>

import urllib2
from bs4 import BeautifulSoup
import re
import htmltagfilter
import time
import config

def getGameInfo(appid):
	appid = str(appid)
	#url = 'https://steamdb.info/app/293400/info/'
	url = 'https://steamdb.info/app/'+appid+'/info/'
	isFailed = True
	print 'connecting'
	while isFailed:
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			request = urllib2.Request(url,headers=headers)
			response = urllib2.urlopen(request)
			read_response = response.read()
			#read_response.decode('utf-8')
			soup = BeautifulSoup(read_response)
			isFailed = False
			print 'access sucessfully!'
		except urllib2.URLError, e:
			print 'game info request denied by server'
			if hasattr(e,"code"):
				print e.code
			if hasattr(e,"reason"):
				print e.reason
			isFailed = True
			time.sleep(config.RETRYTIMEINTERVAL)
	
	
	#To be developed
	gameinfo = dict()
	
	#['appid', 'appname','apptype','releasedate','genre']
	#get game name, genre,  developer, from page
	#blocks = soup.find_all('div',class_='details_block')
	strres = str(read_response)
	pattern_gamename = re.compile('Name</td>([\s\S]*?)</td')
	pattern_type = re.compile('App Type</td>([\s\S]*?)</td') #Game
	pattern_genre = re.compile('Genres</td>([\s\S]*?)</td')
	pattern_developer = re.compile('<td><span itemprop="author">([\s\S]*?)</span')
	pattern_release = re.compile('Release Date</td>([\s\S]*?)</td')
	
	pattern_sub = re.compile('\n')
	pattern_sub2 = re.compile('\(\)')
	
	name = pattern_sub.sub('',htmltagfilter.filter_tags(pattern_gamename.findall(strres)[0]))
	gtype = pattern_sub.sub('',htmltagfilter.filter_tags(pattern_type.findall(strres)[0]))
	genre = pattern_sub.sub('',htmltagfilter.filter_tags(pattern_genre.findall(strres)[0]))
	developer = pattern_sub.sub('',htmltagfilter.filter_tags(pattern_developer.findall(strres)[0]))
	release = pattern_sub.sub('',htmltagfilter.filter_tags(pattern_release.findall(strres)[0]))
	release = pattern_sub2.sub('',release).strip()
	
	if not gtype == 'Game':
		print 'Not a game, record abandon'
		return False
	
	gameinfo['name']=name
	gameinfo['gtype'] = gtype
	gameinfo['genre']=genre
	gameinfo['developer']=developer
	gameinfo['release']=release
	
	print gameinfo
	return gameinfo

if __name__ == '__main__':
	getGameInfo('293400')
	