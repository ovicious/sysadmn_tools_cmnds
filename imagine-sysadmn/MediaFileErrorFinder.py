

###############################
## Error finder

from mutagen.mp3 import MP3
import os

with open("/tmp/imagine-works/error-songs.txt", "r+") as errorfile:



    txs = Track.objects.all()[:5]

    for tx in txs:
        filepath = '/racecdn/media/' + str(tx.original)

        if filepath.endswith('.mp3'):
            try:
                file_info = MP3(filepath)
                file_bitrate = int(file_info.info.bitrate/1000)
                print(filepath,"=",file_bitrate)

            except:
                trackid=tx.id
                errorfile.write(" %s - %s\n" %tx.id %file %)
                


