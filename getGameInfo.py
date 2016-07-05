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
import ujson
import json

def getGameInfo(appid):
	appid = str(appid)
	#url = 'https://steamdb.info/app/293400/info/'
	url = 'http://store.steampowered.com/api/appdetails?appids='+appid
	isFailed = True
	print 'connecting'
	while isFailed:
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			request = urllib2.Request(url,headers=headers)
			response = urllib2.urlopen(request)
			read_response = response.read()
			#read_response.decode('utf-8')
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
	result = json.loads(str(read_response))
	#print result['293400']['data']['genres'].keys()
	type = result[appid]['data']['type']
	Genres = result[appid]['data']['genres']
	name = result[appid]['data']['name']
	developer = result[appid]['data']['developers'][0]
	release = result[appid]['data']['release_date']['date']
	
	genres = list()
	for g in Genres:
		genres.append(g['description'])
		
	if not (type == 'game' or type=='dlc'):
		print 'Not a game, record abandon'
		return False
	
	gameinfo['appid']=appid
	gameinfo['name']=name
	gameinfo['gtype'] = type
	gameinfo['genres']=genres
	gameinfo['developer']=developer
	gameinfo['release']=release
	
	#print gameinfo
	return gameinfo

if __name__ == '__main__':
	getGameInfo('293400')
	