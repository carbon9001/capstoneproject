#this is the main file for crawling data

#pseudo code

#get in the steam's store of a specific game type page
#get the total game number

#for all the pages (give a limit here)
	#get all the app id from that page
		#for each id
		#start getting the reviews of the game's id
		#store the result in files
#after done ,page + 1


import config

# this url is for the 'browse by genre' page
steam_url = config.STEAMURL

#get all the game's appid from the 'browse by genre' page by page
appidlist = list()

