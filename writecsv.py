import csv
import os.path
from Appreview import *
import cStringIO
import codecs
import config

#To be developed: write csv file as append for gameinfo

class DictUnicodeWriter(object):

    def __init__(self, f, fieldnames, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, D):
        self.writer.writerow({k:v.encode("utf-8") for k,v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for D in rows:
            self.writerow(D)

    def writeheader(self):
        self.writer.writeheader()
			

def writecsv_gamecomment(appid, appreview, filedir, rewrite): #(string, object, string, boolean) #filename should end with /
	userid = appreview.userid
	helpfulreview = appreview.hview
	totalreview = appreview.tview
	funnyreview = appreview.fview
	recommanded = appreview.recommanded
	hours = appreview.hours 
	date_posted = appreview.date_posted
	review_content = appreview.review_content
	
	if os.path.isfile(filedir): #add the file name here
		if rewrite:
			#try :
			with open(filedir, 'wb') as csvfile:
				fieldnames = ['appid','userid', 'helpfulreview','totalreview','funnyreview','recommanded','hours','date_posted','review_content']
				writer = DictUnicodeWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				for i in xrange(len(userid)):
					writer.writerow({'appid':str(appid),'userid':userid[i], 'helpfulreview':helpfulreview[i],'totalreview':totalreview[i],'funnyreview':funnyreview[i],'recommanded':str(recommanded[i]),'hours':hours[i],'date_posted':date_posted[i],'review_content':review_content[i]})	
			print 'written to csvfile sucessfully!'
			return True
			#except:
			#	print 'Unknown problem for writting comment csv for app'+str(appid)+' for writecsv_gamecomment() in file writecsv.py'
			#	return False
		else:
			print 'sorry the file has exist in '+ filedir
			return False
	else:
		print 'no such file exists,creating new file'
		with open(filedir, 'wb') as csvfile:
			fieldnames = ['appid','userid', 'helpfulreview','totalreview','funnyreview','recommanded','hours','date_posted','review_content']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in xrange(len(userid)):
				writer.writerow({'appid':str(appid),'userid':userid[i], 'helpfulreview':helpfulreview[i],'totalreview':totalreview[i],'funnyreview':funnyreview[i],'recommanded':recommanded[i],'hours':hours[i],'date_posted':date_posted[i],'review_content':review_content[i]})	
		print 'written to csvfile sucessfully!'
		return True
		

def writecsv_gameinfo(gameinfo,rewrite): #game info here is a string
	appid = gameinfo['appid']
	#this is for writting the information of game
	#filepath = config.CSVPATH+str(game_genre)+'.csv'
	filepath = config.APPINFO
	if os.path.isfile(filepath):
		if rewrite: #rewrite the original gameinfo
			try :
				with open(filepath, 'wb') as csvfile:
					fieldnames = ['appid', 'appname','apptype','release_date','genres','developer','review_number']
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					#writer.writeheader()
					writer.writerow({'appid':appid, 'appname':gameinfo['name'],'apptype':gameinfo['gtype'],'release_date':gameinfo['release'],'genres':gameinfo['genres'],'developer':gameinfo['developer'],'review_number':gameinfo['reviewnum']})
				print 'written to gameinfo sucessfully!'
				return True
			except:
				print 'Unknown problem for writting comment csv for app '+str(appid)+' for writecsv_gamecomment() in file writecsv.py'
				return False
		else:# append to original gameinfo file
			try :
				with open(filepath, 'ab') as csvfile:
					fieldnames = ['appid', 'appname','apptype','release_date','genres','developer','review_number']
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					writer.writerow({'appid':appid, 'appname':gameinfo['name'],'apptype':gameinfo['gtype'],'release_date':gameinfo['release'],'genres':''.join(gameinfo['genres']),'developer':gameinfo['developer'],'review_number':gameinfo['reviewnum']})
				print 'written to gameinfo sucessfully!'
				return True
			except:
				print 'Unknown problem for writting comment csv for app '+str(appid)+' for writecsv_gamecomment() in file writecsv.py'
				return False
	else:#new gameinfo file
		try :
			with open(filepath, 'ab') as csvfile:
				fieldnames = ['appid', 'appname','apptype','release_date','genres','developer']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerow({'appid':appid, 'appname':gameinfo['name'],'apptype':gameinfo['gtype'],'release_date':gameinfo['release'],'genres':gameinfo['genres'],'developer':gameinfo['developer']})
			print 'create and write to gameinfo sucessfully!'
			return True
		except:
			print 'Unknown problem for writting comment csv for app '+str(appid)+' for writecsv_gamecomment() in file writecsv.py'
			return False

def writegameinfoheader():
	filepath = config.APPINFO
	try :
		with open(filepath, 'wb') as csvfile:
			fieldnames = ['appid', 'appname','apptype','release_date','genres','developer','review_number']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			#writer.writerow({'appid':appid, 'appname':gameinfo['name'],'type':gameinfo['gtype'],'release_date':gameinfo['release'],'genres':gameinfo['genres'],'developer':gameinfo['developer'],'review_number':gameinfo['reviewnum']})
		print 'header written for new csv'
		return True
	except:
		print 'Failed to write gameinfo header'
		return False
	


def appendcsv_gamecomment():
	print 'Not developed of appendcsv_gamecomment() in writecsv.py'
	return True
	
def appendcsv_gameinfo():
	print 'Not developed of appendcsv_gamecomment() in writecsv.py'
	return True