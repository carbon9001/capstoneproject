import config
from getCommentByGame import getCommentByGame
from getGameInfo import getGameInfo
from writecsv import writecsv_gameinfo
from writecsv import writegameinfoheader
import pandas as pd
from commentNumber import getTotalReviewNumber
import os.path

def main():
	appidlistdir = config.APPLIST
	appidscrapeddir = config.APPLISTSCRAPED
	appinfodir = config.APPINFO
	gamecount=0

	appidall = list()
	if os.path.isfile(appidlistdir):
		with open(appidlistdir,'rb') as f:
			for line in f:
				if not line in appidall:
					line = str(int(line))
					appidall.append(line)
				else:
					print line + ' has existed!'
	else:
		print 'please create a applist to scrape'

	if os.path.isfile(appidscrapeddir):
		with open(appidscrapeddir,'rb') as f:
			for line in f:
				if line in appidall:
					appidall.remove(line)
				else:
					print line + 'not recorded'
	else:
		f = file(appidscrapeddir,'wb')
		print 'scrapedlist created'

	if os.path.isfile(appinfodir):
		df_info = pd.read_csv(appinfodir)
	else:
		f = file(appinfodir,'wb')
		writegameinfoheader()
		df_info = pd.read_csv(appinfodir)
		print 'gameinfo exist'

	for app in appidall:
		if not app in df_info['appid']:
			gamecount+=1
			appinfo = getGameInfo(app)
			try:
				num_review = getTotalReviewNumber(app)
			except:
				num_review = 0
			appinfo['reviewnum'] = num_review
			print str(appinfo)+' no.'+ str(gamecount)
			writecsv_gameinfo(appinfo,config.GAMEINFOOVERWRITE)
			#getCommentByGame(app,'test',num_review)
			getCommentByGame(app,'test',num_review)
			#at last add the app to the readlist
			f = open(appidscrapeddir,'ab')
			f.write(app+'\n')
			f.close()
		else:
			print 'game info of '+app+' has been recorded'

if __name__=='__main__':
	main()