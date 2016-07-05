
import urllib2
from bs4 import BeautifulSoup
import re
import htmltagfilter
from Appreview import *
import time
import config

#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&numperpage=10&browsefilter=toprated&browsefilter=toprated&l=english&appHubSubSection=10&filterLanguage=default&searchText=&forceanon=1'
#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=271590&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=5000&browsefilter=toprated&appid=271590&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'

#this function access to comment dirrectly from its javascript interface
#it return a Appreview Object

#To be developed: see whether the user id has been recorded

def getCommentInPage(appid,reviewoffset,page):
	
	appid = str(appid)
	reviewoffset = str(reviewoffset)
	page = str(page)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	url = 'http://steamcommunity.com/app/'+appid+'/homecontent/?userreviewsoffset='+reviewoffset+'&p='+page+'&workshopitemspage='+page+'readytouseitemspage='+page+'&mtxitemspage='+page+'&itemspage='+page+'&screenshotspage='+page+'&videospage='+page+'&artpage='+page+'&allguidepage='+page+'&webguidepage='+page+'&integratedguidepage='+page+'&discussionspage='+page+'&numperpage=1'+page+'&browsefilter=toprated&appid='+appid+'&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
#	url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=0&p=4&workshopitemspage=4&readytouseitemspage=4&mtxitemspage=4&itemspage=4&screenshotspage=4&videospage=4&artpage=4&allguidepage=4&webguidepage=4&integratedguidepage=4&discussionspage=4&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=271590&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
	
	
	isFailed = True
	while isFailed:
		try:
			request = urllib2.Request(url,None,headers)
			response = urllib2.urlopen(request)
			read_response = response.read()
			#read_response.decode('utf-8')
			soup = BeautifulSoup(read_response)
			isFailed = False
		except urllib2.URLError, e:
			if hasattr(e,"code"):
				print e.code
			if hasattr(e,"reason"):
				print e.reason
			isFailed = True
			time.sleep(config.RETRYTIMEINTERVAL)
			
	if int(page)%config.PAGEPROGRESSRESOLUTION==0:			
		print 'crawling page '+page+' for app '+str(appid),
	userid = list()
	helpfulreview = list()
	totalreview = list()
	funnyreview = list()
	recommanded = list()
	date_posted = list()
	hours = list()
	review_content=list()
	subsouplist=soup.find_all('div',class_= 'apphub_Card modalContentLink interactable')
	for s in subsouplist:
		soup = BeautifulSoup(str(s))
		hasget=False
		user_herf = soup.find_all('div',class_='apphub_CardContentAuthorName')
		pattern = re.compile(r"((?<=http://steamcommunity.com/id/).+?(?=/))|((?<=http://steamcommunity.com/profiles/).+?(?=/))")
		#userid = list()
		for user_iter in user_herf:
			tp = pattern.findall(str(user_iter),re.I|re.S|re.M)[0]
			if (tp[0]==''):
				userid.append(str(tp[1]))
				hasget = True
			else:
				userid.append(str(tp[0]))
				hasget = True
		if len(user_herf)==0:
			tp=pattern.findall(str(s))[0]
			if (tp[0]==''):
				userid.append(tp[1])
				hasget = True
			else:
				userid.append(tp[0])
				hasget = True
		
		helpful = soup.find_all('div',class_='found_helpful')
		pattern = re.compile(r'\d.*(?= of)')
		#helpfulreview = list()
		for review in helpful:
			tp = pattern.findall(str(review),re.I|re.S|re.M)
			if tp:
				helpfulreview.append(tp[0])
				if not hasget:
					hasget = False
				else:
					hasget = True
			else:
				helpfulreview.append('0')
				#print 'no help review!'
		
		
		#print helpfulview

		pattern = re.compile(r'(?<=of )\d.*(?= people \()')
		#totalreview = list()
		for review in helpful:
			tp = pattern.findall(str(review),re.I|re.S|re.M)
			if tp:
				totalreview.append(tp[0])
				if not hasget:
					hasget = False
				else:
					hasget = True
			else:
				totalreview.append('0')
				#print 'no total review!'
		#print totalview

		pattern = re.compile(r'(?<=\<br/\>)\d.*(?= people)')
		#funnyreview = list()
		for review in helpful:
			tp = pattern.findall(str(review),re.I|re.S|re.M)
			if tp:
				funnyreview.append(tp[0])
			else:
				funnyreview.append('0')
				#print 'no funny review number'
		#print funnyreview

		recommand = soup.find_all('div',class_='title')
		#recommanded = list()
		pattern = re.compile('Not Recommended')
		for r in recommand:
			if r.string == 'Not Recommended':
				recommanded.append(False)
			else:
				recommanded.append(True)
			if not hasget:
				hasget = False
			else:
				hasget = True
		#print recommanded

		#hours = list()
		hrs = soup.find_all('div',class_='hours')
		pattern = re.compile(r'\d.*(?= hrs)')
		for h in hrs:
			tp = pattern.findall(str(h))
			hours.append(tp[0])
		#print hours

		#date_posted = list()
		dp = soup.find_all('div',class_='date_posted')
		pattern = re.compile(r'(?<=Posted: ).*(?=</div>)')
		for d in dp:
			tp = pattern.findall(str(d),re.I|re.S|re.M)
			date_posted.append(tp[0])
			if not hasget:
				hasget = False
			else:
				hasget = True
		#print date_posted


		reviews = soup.find_all('div',class_="apphub_CardTextContent")
		pattern = re.compile(r'<div class="date_posted">[^<]*</div>\s*(.*)')
		#review_content=list()
		for rc in reviews:
			#print str(rc)
			tp = pattern.findall(str(rc),re.S)[0]
			if tp:
				pass
				if not hasget:
					hasget = False
				else:
					hasget = True
			else:
				print "No match"
			tp = htmltagfilter.filter_tags(tp)
			review_content.append(tp)
		if not hasget:
			print 'Some components cannot be found!'
		#print userid
		#print helpfulreview
	comments = Appreview(appid=appid,userid=userid,hview=helpfulreview,tview=totalreview,fview=funnyreview,recommanded=recommanded,hours=hours,date_posted=date_posted,review_content=review_content)	
	print 'number of comments: '+str(len(userid))
	return comments

if __name__=='__main__':
	print 'testing mode for getCommentInPage for GTA5 at page 1'
	getCommentInPage('271590',0,1)


