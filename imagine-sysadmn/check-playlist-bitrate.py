
#take one playlist

#Check all tracks and its bitrate

#

import os


for pls in Playlist.objects.all():  
	#show all playlist ids and titles
	print(pls.id,pls.title)
