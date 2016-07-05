htmlcontent = '''
<div class="apphub_Card modalContentLink interactable" data-modal-content-sizetofit="false" data-modal-content-url="http://steamcommunity.com/profiles/76561198064850410/recommended/271590/" style="display: none">
<div class="apphub_CardContentMain">
<div class="apphub_UserReviewCardContent">
<div class="found_helpful">
                                768 of 981 people (78%) found this review helpful<br/>522 people found this review funny                        </div>
<div class="vote_header">
<div class="reviewInfo">
<div class="thumb">
<img height="44" src="http://steamcommunity-a.akamaihd.net/public/shared/images/userreviews/icon_thumbsUp.png?v=1" width="44"/>
</div>
<div class="title">Recommended</div>
<div class="hours">45.9 hrs on record</div>
</div>
<div style="clear: left"></div>
</div>
<div class="apphub_CardTextContent">
<div class="date_posted">Posted: April 14, 2015</div>
                                                                                                The tennis ini game ?is more mechanically in depth than other games that focused exclusively on making a tennis game. Apparently.. there is even more than just tennis in this game!<br/><br/><i>Join the Council of Space Dragons <a class="bb_link" href="http://steamcommunity.com/groups/space-dragons#curation" rel="noreferrer" target="_blank">here.</a> Breaching the impasse beyond Omega 4.</i> </div>
</div>
<div class="UserReviewCardContent_Footer">
<div class="gradient">233</div>
</div>
</div>
<div class="apphub_CardContentAuthorBlock tall">
<div class="apphub_friend_block_container">
<a href="http://steamcommunity.com/profiles/76561198064850410/">
<div class="apphub_friend_block" data-miniprofile="104584682">
<div class="appHubIconHolder online"><img src="http://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/5a/5a1d5bb2d3935c45d37399dd8f07c8cb6a8752ec.jpg"/></div>
<div class="appHubIconHolder greyOverlay"></div>
<div class="apphub_CardContentAuthorName online ellipsis"><a href="http://steamcommunity.com/profiles/76561198064850410/">SpaceCouncil</a></div>
<div class="apphub_CardContentMoreLink ellipsis">1,442 products in account</div>
</div>
</a>
</div>
<div class="apphub_UserReviewCardStats">
<div class="apphub_CardCommentCount alignNews">19</div>
</div>
<div style="clear: left"></div>
</div>
</div>

								'''

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(htmlcontent)
#subsouplist=soup.find_all('div',class_= 'apphub_CardContentMain')
subsouplist=soup.find_all('div',class_= 'apphub_Card modalContentLink interactable')
helpfulview = list()
funnyview=list()
recommanded = list()
hours = list()
date_posted = list()
review_content=list()
#print len(subsouplist)
#print subsouplist[0]

for s in subsouplist:
	soup = BeautifulSoup(str(s))
	
	user_herf = soup.find_all('div',class_='apphub_CardContentAuthorName')
	pattern = re.compile(r"((?<=http://steamcommunity.com/id/).+?(?=/))|((?<=http://steamcommunity.com/profiles/).+?(?=/))")
	#userid = list()
	for user_iter in user_herf:
		tp = pattern.findall(str(user_iter),re.I|re.S|re.M)[0]
		if (tp[0]==''):
			userid.append(str(tp[1]))
		else:
			userid.append(str(tp[0]))
	if len(user_herf)==0:
		tp=pattern.findall(str(s))
		print tp
	helpful = soup.find_all('div',class_='found_helpful')
	pattern = re.compile(r'\d.*(?= of)')
	#print len(helpful)
	#helpfulview = list()
	for review in helpful:
		tp = pattern.findall(str(review),re.I|re.S|re.M)
		helpfulview.append(tp)
	#print helpfulview

	pattern = re.compile(r'(?<=<br/>)\d.*(?= people)')
	#funnyview = list()
	for review in helpful:
		tp = pattern.findall(str(review),re.I|re.S|re.M)
		funnyview.append(tp)
	#print funnyview

	recommand = soup.find_all('div',class_='title')
	#recommanded = list()
	pattern = re.compile('Not Recommended')
	for r in recommand:
		if r.string == 'Not Recommended':
			recommanded.append(False)
		else:
			recommanded.append(True)
	#print recommanded

	#hours = list()
	hrs = soup.find_all('div',class_='hours')
	pattern = re.compile('\d.*(?= hrs)')
	for h in hrs:
		tp = pattern.findall(str(h))
		hours.append(tp)
	#print hours

	#date_posted = list()
	dp = soup.find_all('div',class_='date_posted')
	pattern = re.compile(r'(?<=Posted: ).*(?=</div>)')
	for d in dp:
		tp = pattern.findall(str(d),re.I|re.S|re.M)
		date_posted.append(tp)
	#print date_posted

	for linebreak in soup.find_all('br'):
		#print linebreak
		linebreak.extract()

	reviews = soup.find_all('div',class_="apphub_CardTextContent")
	pattern = re.compile(r'<div class="date_posted">[^<]*</div>\s*(.*)')
	#review_content=list()
	# for lb in soup.find_all('br'):
		# lb.extract()
	for rc in reviews:
		tp = pattern.findall(str(rc),re.S)
		
		review_content.append(tp)

	# reviews = soup.find_all('div',class_="date_posted")
	# for rc in reviews:
		# print str(rc.next_sibling)
		# print str(rc.next_sibling)
		# tp = pattern.search(rc.next_sibling,re.S|re.M)
		# review_content.append([str(rc.next_sibling)])

print userid
print helpfulview
print funnyview
print recommanded
print hours
print date_posted
print len(review_content)