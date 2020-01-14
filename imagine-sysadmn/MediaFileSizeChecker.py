###############################
# Size checker

import os                                                                                                          
from mutagen.mp3 import MP3                                                                                        
from shutil import copyfile                                                                               
object_id_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/error-songs.txt')]                 
txs = Track.objects.all().order_by('id').filter(status='published').exclude(id__in=object_id_list)              
countTotal=0
count128=0
count192=0
count320=0
totalfilesize=0
totalfilesize128=0
totalfilesize192=0
totalfilesize320=0

for tx in txs:                                                                                                  
    filepath = '/racecdn/media/' + str(tx.original)                                                             
                                                                                                                
    if filepath.endswith('.mp3'):                                                                               
                                                                                                                
        file_info = MP3(filepath)                                                                               
        file_bitrate = int(file_info.info.bitrate/1000)                                                         
                                                                                                                
        #print(tx.id)                                                                                            
        #print(filepath)                                                                                         
        #print(file_bitrate)  
                                                                                                          
        songname = filepath.rsplit('/',1)[1][:-4]                                                               
        countTotal +=1
        filesize = os.path.getsize(filepath)
        totalfilesize+=filesize
        if file_bitrate > 127 and file_bitrate < 192:

            filesize = os.path.getsize(filepath)
            totalfilesize128+=filesize
            count128+=1

        if file_bitrate > 191 and file_bitrate < 320 :

            filesize = os.path.getsize(filepath)
            totalfilesize192+=filesize
            count192+=1
        if file_bitrate > 319:

            filesize = os.path.getsize(filepath)
            totalfilesize320+=filesize
            count320+=1

print("128kbps files = ",count128, " and total ",totalfilesize128, " bytes")
print("192kbps files = ",count192, " and total ",totalfilesize192, " bytes")
print("128kbps files = ",count320, " and total ",totalfilesize320, " bytes")
