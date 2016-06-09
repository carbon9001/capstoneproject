
import urllib2
from bs4 import BeautifulSoup
import re

page = 1
#url = 'http://steamcommunity.com/app/371590/reviews/?browsefilter=toprated&filterLanguage=english'
#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&numperpage=10&browsefilter=toprated&browsefilter=toprated&l=english&appHubSubSection=10&filterLanguage=default&searchText=&forceanon=1'
#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=271590&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=0&p=4&workshopitemspage=4&readytouseitemspage=4&mtxitemspage=4&itemspage=4&screenshotspage=4&videospage=4&artpage=4&allguidepage=4&webguidepage=4&integratedguidepage=4&discussionspage=4&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=271590&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
#url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=5000&browsefilter=toprated&appid=271590&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'

appid = ''
reviewoffset = ''


def getCommentInPage(appid,reviewoffset,page):

#	url = 'http://steamcommunity.com/app/'+appid+'/homecontent/?userreviewsoffset='+reviewoffset+'&p='+page+'&workshopitemspage='+page+'readytouseitemspage='+page+'&mtxitemspage='+page+'&itemspage='+page+'&screenshotspage='+page+'&videospage='+page+'&artpage='+page+'&allguidepage='+page+'&webguidepage='+page+'&integratedguidepage='+page+'&discussionspage='+page+'&numperpage=1'+page+'&browsefilter=toprated&appid='+appid+'&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
	url = 'http://steamcommunity.com/app/271590/homecontent/?userreviewsoffset=0&p=4&workshopitemspage=4&readytouseitemspage=4&mtxitemspage=4&itemspage=4&screenshotspage=4&videospage=4&artpage=4&allguidepage=4&webguidepage=4&integratedguidepage=4&discussionspage=4&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=271590&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'


	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		read_response = response.read()
		#read_response.decode('utf-8')
		soup = BeautifulSoup(read_response)
	except urllib2.URLError, e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason  

	user_herf = soup.find_all('div',class_='apphub_CardContentAuthorName')
	pattern = re.compile(r"((?<=http://steamcommunity.com/id/).+?(?=/))|((?<=http://steamcommunity.com/profiles/).+?(?=/))")
	userid = list()
	for user_iter in user_herf:
		tp = pattern.findall(str(user_iter),re.I|re.S|re.M)[0]
		if (tp[0]==''):
			userid.append(tp[1])
		else:
			userid.append(tp[0])

	helpful = soup.find_all('div',class_='found_helpful')
	pattern = re.compile(r'\d.*(?= of)')
	helpfulview = list()
	for review in helpful:
		tp = pattern.findall(str(review),re.I|re.S|re.M)
		helpfulview.append(tp)
	#print helpfulview

	pattern = re.compile(r'(?<=of )\d.*(?= people \()')
	totalview = list()
	for review in helpful:
		tp = pattern.findall(str(review),re.I|re.S|re.M)
		totalview.append(tp)
	#print totalview

	pattern = re.compile(r'(?<=\<br/\>)\d.*(?= people)')
	funnyview = list()
	for review in helpful:
		tp = pattern.findall(str(review),re.I|re.S|re.M)
		funnyview.append(tp)
	#print funnyview

	recommand = soup.find_all('div',class_='title')
	recommanded = list()
	pattern = re.compile('Not Recommended')
	for r in recommand:
		if r.string == 'Not Recommended':
			recommanded.append(False)
		else:
			recommanded.append(True)
	#print recommanded

	hours = list()
	hrs = soup.find_all('div',class_='hours')
	pattern = re.compile(r'\d.*(?= hrs)')
	for h in hrs:
		tp = pattern.findall(str(h))
		hours.append(tp)
	#print hours

	date_posted = list()
	dp = soup.find_all('div',class_='date_posted')
	pattern = re.compile(r'(?<=Posted: ).*(?=</div>)')
	for d in dp:
		tp = pattern.findall(str(d),re.I|re.S|re.M)
		date_posted.append(tp)
	#print date_posted


	reviews = soup.find_all('div',class_="apphub_CardTextContent")
	pattern = re.compile(r'<div class="date_posted">[^<]*</div>\s*(.*)')
	review_content=list()
	for rc in reviews:
		#print str(rc)
		tp = pattern.findall(str(rc),re.S)
		if tp:
			pass
		else:
			print "No match"
		review_content.append(tp)

if __name__=='__main__':
	getCommentInPage('1','1','1')


