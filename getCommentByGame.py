
#num of to be developed: 1

#get the number of comments in this game
#get comments in the game using getCommentByPage
import config
import getCommentInPage
from Appreview import *
import writecsv
import time
import sys
from commentNumber import getTotalReviewNumber

reload(sys)
sys.setdefaultencoding('utf8')

def getCommentByGame(appid,appmaingenre,reviewnumber):
	page = 1
	reviewoffset = 0
	reviewperpage = 10 #this value seems cannot be change
	
	#num_review = 2000
	num_review = reviewnumber
	
	num_page = num_review/reviewperpage
	
	#path for write the game comments csv file
	#filedir = config.CSVPATH+str(appmaingenre)+'/'+str(appid)+'.csv'
	filedir = config.CSVPATH+str(appid)+'.csv'
	print filedir
	
	print 'crawling reviews from game '+str(appid)
	#get the comments page by page
	allreview = Appreview(appid = appid)
	add=False
	for i in xrange(num_page):
		if not add:
			zerocount=0
		review = getCommentInPage.getCommentInPage(appid,reviewoffset,page)
		allreview.merge_appreview(review)
		if len(review.userid)==0:
			add=True
			zerocount+=1
		else:
			add = False
		if zerocount>5:
			print 'not getting proper response!'
			break;
		time.sleep(config.TIMEINTERVAL)
		page += 1
		reviewoffset+=reviewperpage
	
	print str(len(allreview.userid))+' reviews of '+str(appid)+ ' has been obtained!',
	
	writecsv.writecsv_gamecomment(appid, allreview, filedir, config.COMMENTOVERWRITE)

if __name__ == '__main__':
	print 'testing mode for GTA5'
	appid = '271590'
	try:
		num_review = getTotalReviewNumber(appid)
	except:
		print 'some problem in getting Review Number for app'+' '+appid
	print 'the total number of review is '+str(num_review)
	num_review = getTotalReviewNumber('271590')
	getCommentByGame(appid,'test',num_review)

	
