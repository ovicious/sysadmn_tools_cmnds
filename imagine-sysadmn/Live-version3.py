playlist = Playlist.objects.filter(genre=Genre.objects.get(pk=178))
tracks = Playlist.objects.filter(id__in=playlist).values_list('tracks__original')


import itertools

trs = list(itertools.chain(*tracks))

ftrs = []

for a in trs:
	if a is not None:
		ftrs.append(a)

with open('stream.txt', 'w') as f:
    for item in ftrs:
        f.write("%s\n" % item.replace('tracks/', '/racecdn/media/tracks/'))