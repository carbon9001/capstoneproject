from bs4 import BeautifulSoup
import re
import htmltagfilter

read_response = str(open('gameinfosample.html').read())


soup = BeautifulSoup(read_response)

#To be developed
gameinfo = dict()
#get game mode from page
blocks = soup.find_all('div',class_='block responsive_apppage_details_left')
modestr = htmltagfilter.filter_tags(str(blocks))
print modestr
modestr = [i for i in modestr.split()]
	
#['appid', 'appname','releasedate','genre','gamemode']
#get game name, genre,  developer, from page
blocks = soup.find_all('div',class_='details_block')
pattern_gamename = re.compile('Title:</b>(.*?)<')
pattern_genre = re.compile('Genre:</b>([\s\S]*?)<br>')
pattern_developer = re.compile('Developer:</b>([\s\S]*?)<br>')
pattern_release = re.compile('Release Date:</b>([\s\S]*?)<br>')
for b in blocks:
	name = htmltagfilter.filter_tags(pattern_gamename.findall(str(blocks)))
	genre = htmltagfilter.filter_tags(pattern_genre.findall(str(blcoks)))
	developer = htmltagfilter.filter_tags(pattern_developer.findall(str(blocks)))
	release = htmltagfilter.filter_tags(pattern_release.findall(str(blocks)))

gameinfo['name']=name
gameinfo['genre']=genre
gameinfo['developer']=developer
gameinfo['release']=release

print gameinfo