playlist = Playlist.objects.filter(status='published',genre=Genre.objects.get(pk=227))
#pk = Genre ID
tracks = Playlist.objects.filter(id__in=playlist).values_list('tracks__original')
  

import itertools

trs = list(itertools.chain(*tracks))

ftrs = []

for a in trs:
    if a is not None:
        ftrs.append(a)

with open('ir-ch106-lullabiesforwinter.txt', 'w') as f:
    for item in ftrs:
        f.write("%s\n" % item.replace('tracks/', '/racecdn/media/tracks/'))

