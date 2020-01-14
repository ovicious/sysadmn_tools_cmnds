import os.path
import sqlite3 as sq3
from mutagen import File as mfile
import django
from django.core.files import File
from django.db.models import Count

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

from apps.songs.models import Track, Album, Artist, Playlist

#px=all playlists
px = Playlist.objects.all()

#NEED TO Understand
dup = Track.objects.values('title','artist','album').annotate(Count('id')).order_by().filter(id__count__gt=1)

for d in dup:

	tx = Track.objects.filter(title=d['title'],artist=d['artist'],album=d['album'])

	print('=====================================')
	print(str(d['title']) + ' - Artist:' + str(d['artist']) + ' - Album:' + str(d['album']))
	print('=====================================')

	fixed_track_pk = tx[0].pk

	tx_array = []

	for t in tx:
		filepath = '/racecdn/media/' + str(t.original)
		if os.path.isfile(filepath):
			fixed_track_pk = t.pk
		
		tx_array.append(t.pk)

	for p in px:

		ptracks = p.tracks.values_list('id',flat=True)

		if set(tx_array) & set(ptracks):
			print('Playlist - ' + str(p.pk) + ' - ' + p.title)
			for t in tx:
				if t.pk == fixed_track_pk:
					p.tracks.add(t)
					print(str(t.pk) + '-' + str(t.title) + ' - Added to - ' + str(p.pk) + '-' + str(p.title))		
		else:
					p.tracks.remove(t)
					print(str(t.pk) + '-' + str(t.title) + ' - Deleted from - ' + str(p.pk) + '-' + str(p.title))