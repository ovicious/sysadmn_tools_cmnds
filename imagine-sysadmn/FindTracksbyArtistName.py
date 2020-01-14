import os
from mutagen.mp3 import MP3
from shutil import copyfile


artist_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/artist-list-raju-vai.txt')]

for arti in artist_list:
    a = Artist.objects.filter(title__iexact=arti)[0]
    c = Album.objects.filter(artist__iexact=a)
    print(len(c))
    print(a)







##############
##by Rokon

artist_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/artist-list-raju-vai.txt')]
                                                                   
for arti in artist_list:
    try:
        artist = Artist.objects.filter(title__iexact=arti)
        print ("Artist Name : ", artist[0].title)
        album_count = Album.objects.filter(artist__iexact=artist[0]).count()      
        print("Album Count : ",album_count)                         
        track_count = Track.objects.filter(artist__iexact=artist[0]).count() 
        print("Track Count : ",track_count)             
    except:                                                         
        print (arti," Not Found")                                   
    print(" .............................. ")       



#################################
## my code working

import os.path
import sqlite3 as sq3
from mutagen import File as mfile
import django
from django.conf import settings
from django.core.files import File


os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

from apps.songs.models import Track, Album, Artist, Playlist, SelectedPlaylists



artist_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/artist-list-raju-vai.txt')]
errors = []
for arti in artist_list:
    try:

        target_artist = Artist.objects.get(title__iexact=arti)
        #print(arti_title.title)                                      
        artist_albums = Album.objects.filter(artist=target_artist)
        print("Artist = ",arti)                                                     
        
        for album in artist_albums:
            print("Album = ",album.title,"Album ID = ", album.id )

            artist_tracks = Track.objects.filter(album = album)
            print("Tracks:")
            for track in artist_tracks:
                print (track.title)
            print(".................................")

        print("==============================================")


        
    except:

        errors.append(arti)
        
print(errors)



###### Rakib Vai Artist Tracks List

artist_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/rakib-vai-artist-list.txt')]

error = []
for artist in artist_list:
    artist_exist = Artist.objects.filter(title__iexact=artist).count()
    if artist_exist > 0:
        
        track_count = Track.objects.filter(artist__title__iexact=artist).count()
        print(artist," : ",track_count)
        #print(artist)
    else:
        error.append(artist)
            
print("\n Not Found : \n",error)
