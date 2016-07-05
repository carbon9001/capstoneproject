
#merge_appreview(Appreview1,Appreview2): combine 2 Appreview object
#has_commented_user(Appreview,userid): see if the user id exist in Appreview

#init(appid=,userid=,hview=,tview=,fview=,recommanded=,hours=,date_posted=,view_content=)
#pls make sure that the parameters are one by one in order

class Appreview:
	def __init__(self,**kwargs):
		if kwargs:
			if 'userid' in kwargs.keys():
				if len(kwargs['userid'])==len(kwargs['hview']) and len(kwargs['userid'])==len(kwargs['tview']) and len(kwargs['userid'])==len(kwargs['fview']) and len(kwargs['userid'])==len(kwargs['recommanded']) and len(kwargs['userid'])==len(kwargs['hours']) and len(kwargs['userid'])==len(kwargs['review_content']):
					self.appid = kwargs['appid']
					self.userid = list()
					self.userid.extend(kwargs['userid'])
					self.hview=list()
					self.hview.extend(kwargs['hview'])
					self.tview=list()
					self.tview.extend(kwargs['tview'])
					self.fview = list()
					self.fview.extend(kwargs['fview'])
					self.recommanded = list()
					self.recommanded.extend(kwargs['recommanded'])
					self.hours = list()
					self.hours.extend(kwargs['hours'])
					self.date_posted = list()
					self.date_posted.extend(kwargs['date_posted'])
					self.review_content = list()
					self.review_content.extend(kwargs['review_content'])
				else:
					#here is forcing the input has the same lenght due to the problem of wrong design of data structure
					user_num = len('userid')
					self.appid = kwargs['appid']
					self.userid = list()
					self.userid.extend(kwargs['userid'][:user_num])
					self.hview=list()
					self.hview.extend(kwargs['hview'][:user_num])
					self.tview=list()
					self.tview.extend(kwargs['tview'][:user_num])
					self.fview = list()
					self.fview.extend(kwargs['fview'][:user_num])
					self.recommanded = list()
					self.recommanded.extend(kwargs['recommanded'][:user_num])
					self.hours = list()
					self.hours.extend(kwargs['hours'][:user_num])
					self.date_posted = list()
					self.date_posted.extend(kwargs['date_posted'][:user_num])
					self.review_content = list()
					self.review_content.extend(kwargs['review_content'][:user_num])
					print 'Warning! Input List should all have same length for Appreview Object!'
			else:
				self.appid = kwargs['appid']
				self.userid = list()
				self.hview=list()
				self.tview=list()
				self.fview = list()
				self.recommanded = list()
				self.hours = list()
				self.date_posted = list()
				self.review_content = list()
		else:
			self.appid = ''
			self.userid = list()
			self.hview=list()
			self.tview=list()
			self.fview = list()
			self.recommanded = list()
			self.hours = list()
			self.date_posted = list()
			self.review_content = list()
	
	def merge_appreview(self,other):
		if other and self:
			if other.appid == self.appid:
				for i in xrange(len(other.userid)):
					if other.userid[i] not in self.userid :
						self.userid.append(other.userid[i])
						self.hview.append(other.hview[i])
						self.tview.append(other.tview[i])
						self.fview.append(other.fview[i])
						self.recommanded.append(other.recommanded[i])
						self.hours.append(other.hours[i])
						self.date_posted.append(other.date_posted[i])
						self.review_content.append(other.review_content[i])
					else:
						#print 'Warning,'+other.userid[i]+' has been recorded, record abandon'
						pass
			else:
				print 'Error! Comment Not from the same app'
		else:
			print 'for some unknown reason, no appid exsit!'
		return self
	
	#this method merge appreview without considering repetitive userid, not recommanded
	def merge_appreview_force(self,other):
		if other.appid == self.appid:
			self.userid.extend(other.userid)
			self.hview.extend(other.hview)
			self.tview.extend(other.tview)
			self.fview.extend(other.fview)
			self.recommanded.extend(other.recommanded)
			self.hours.extend(other.hours)
			self.date_posted.extend(other.date_posted)
			self.review_content.extend(other.review_content)
		else:
			print 'Error! Comment Not from the same app'
		return self
		
	def has_commented_user(self, uid):
		if uid in self.userid:
			return True
		else:
			return False
	
	