import os.path
import sqlite3 as sq3
from mutagen import File as mfile
import django
from django.conf import settings
from django.core.files import File


os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

from apps.songs.models import Track, Album, Artist, Playlist, SelectedPlaylists

live = SelectedPlaylists.objects.filter(title='Live').values_list('playlists__id', flat=True)
live = list(live)
tracks = Playlist.objects.filter(id__in=live).values_list('tracks__original')
# tracks = Playlist.objects.filter(title='Party-Live').values_list('tracks__original')




import itertools

trs = list(itertools.chain(*tracks))

ftrs = []

for a in trs:
	if a is not None:
		ftrs.append(a)

from shutil import copyfile

for a in ftrs:
	# copyfile(a, replace('tracks/', 'stream/'))
	copyfile('/racecdn/media/' +a, a.replace('tracks/', '20mar/'))

with open('stream.txt', 'w') as f:
    for item in ftrs:
        f.write("%s\n" % item.replace('tracks/', ''))

