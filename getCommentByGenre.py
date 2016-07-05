#need a list for what game id in the type
#in file '%gametype_appinfo.csv' appid, gamename,(if possible, get the game type(multiple type possible))
#
#try to get the number of game
#get game id
#get number of comment in game
#get the comment of the game page by page
#store in csv file

import config
import writecsv
import getCommentByGame
import Appreview
#here is the desire game type(from which game type)
#start at the page of the genre page
#get all the app id of the type from top filter(or specify the name of the app's number)

#To be developed:
def get_number_of_gamebygenre():#add neccessary parameter from here
	#add logic here to get number of game by genre
	num_game = 100
	return num_game

#To be developed
#get the list of 
def get_app_id():
	appid = list()
	return appid
	
def getCommentByGenre(genre):
	number_isset = True
	# to be defined
	gametype = ''
	if number_isset:
		num_game = 100
	else:
		num_game = get_number_of_gamebygenre()


	#To be Developed:
	#for all the game in the genre
		#try to get the info of game (function in this file)
		#then get the comment of the game (function in getCommentByGame)
		#append game info to the genre.csv (call in this file)
		#write the comment of the game into ./comment/genre/gameid.csv(call in this file)
	for i_game in xrange(1:numgame+1):

		
		appid = 
		getCommentByGame(appid,genre)
		

if __name__ = '__main__':
	#to be developed
	genre = 
	getCommentByGame(genre)
