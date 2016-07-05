from bs4 import BeautifulSoup
import re
import urllib2
import urllib
def getTotalReviewNumber(appid):
	#550
	#271590
	appid='550'
	appid = str(appid)
	cookies = {'birthtime': '568022401'}
	url = 'http://store.steampowered.com/app/'+appid
	#request = urllib2.Request(url,cookies=cookies)
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', 'birthtime=568022401'))
	response = opener.open(url)
	#response = urllib2.urlopen(request)
	read_response = response.read()
	soup = BeautifulSoup(read_response,"html.parser")
	#soup = BeautifulSoup(htmlcontent,"html.parser")
	summary = soup.find_all('div',class_='user_reviews_summary_bar')
	#pattern = re.compile(r'<div class="title">Overall[.?\/ *]</span>[.?*]>\((.*?)reviews\)</span')
	pattern = re.compile(r'\((.*?) reviews\)')
	total_number = list()
	b = 0
	for s in summary:
		tp = pattern.findall(str(summary),re.I|re.S|re.M)
		#print tp
		if len(tp)==2:
			b=int(tp[1].replace(',',''))
		elif len(tp)==1:
			b=int(tp[0].replace(',',''))
		else:
			b = 0
	return b
	