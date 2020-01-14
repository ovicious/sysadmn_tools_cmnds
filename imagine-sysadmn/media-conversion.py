193 >= mp3 >= 320kbps
	copy/convert to 320
	convert to 192
	convert to 128  

129 >= mp3 <= 192kbps
	copy/convert to 192
	convert to 128

128 = mp3 	

Video
high=720p
medium=480p
low=320p


for MP3=320 or higher bitrate
	copy 320 MP3 to high
	convert to 320,192,128 and save to high
for MP3=192 to 319
	copy 192 MP3 to medium
	convert to 192,128 and save to medium
for MP3=128 to 191
	copy 128 MP3 to low
	convert to 128 and save to low

###############################################################3
import os
from mutagen.mp3 import MP3

a = Playlist.objects.all()

trs = []                                                                                                                                      
btrs = []                  
strs = []                                                                                                                                     
count = 0                                                                                                                                    
base='/racecdn/media/tracks/'                  
for p in a:                                                                                                                                   
            
    for t in p.tracks.all():                                                                                                               
        trs.append(t.original)
                                                                                                                                             
for t in trs:
    fp = '/racecdn/media/' + str(t)
   # count = count+1                                                                                                
    try:
       # print(count)                                                                                                                        
 
        f = MP3(fp)
        fbr=int(f.info.bitrate/1000)
        print(fbr)
        if fbr > 320 and fp.endswith('.mp3'):
           btrs.append(fp)
           

           base_high = '/racecdn/media/tracks/high/'
           base_medium = '/racecdn/media/tracks/medium/' 
           base_low = '/racecdn/media/tracks/low/'
                                                                  
           songname = fp.rsplit('/',1)[1]                                                  
           new_file_name_high = base_high + songname[:-4] + '_high' + '.mp3';
           new_file_name_medium = base_medium + songname[:-4] + '_medium' + '.mp3';
           new_file_name_low = base_low + songname[:-4] + '_low' + '.mp3';                                           
                                                                        
          #CONVERT TO 320                                                                                        
           my_cmd_high = 'ffmpeg -y -i ' + fp +' -codec:a libmp3lame -b:a 320k ' + new_file_name_high                       
          #CONVERT TO 192                                                                                        
           my_cmd_medium = 'ffmpeg -y -i ' + fp +' -codec:a libmp3lame -b:a 192k ' + new_file_name_medium
          #Convert to 128
           my_cmd_low = 'ffmpeg -y -i ' + fp +' -codec:a libmp3lame -b:a 128k ' + new_file_name_low
          
          #my_cmd = 'ffmpeg -y -i ' + fp +' -codec:a libmp3lame -b:a 320k ' + new_file_name
          #os.system(my_cmd_high)
          #os.system(my_cmd_medium)
          #os.system(my_cmd_low)                                                        
                                                                                                                               
        elif fbr == 320 and fp.endswith('.mp3'):                                                                                    
           #strs.append(fp)
           base_high = '/racecdn/media/tracks/320/'
           songname = fp.rsplit('/',1)[1]                                                                                         
           new_file_name = base_high + songname[:-4] + '_320' + '.mp3';
           print(base_high+songname)
           copyfile(base+songname, new_file_name)
           


   #pass                                                                                                                       
    except:                                                                                                                        
        pass         

###########################################################33
#### OLD Script
import os                                                                                                                                     
                           
from mutagen.mp3 import MP3                                                                                                                   
                                                                                                                                             
                                                                                                                                              
a = Playlist.objects.all()                                                                                                         
trs = []                   
btrs = []                                                                                                                                     
strs = []                     
count = 0                                                                                                                                    
                                                                                                                                   
for p in a:                                                                                                                                   
                                                                                                                   
    for t in p.tracks.all():                                                                                                               
        trs.append(t.original)                                                                                                               
                                                                                                                                   
for t in trs:                                                                                                                                
    fp = '/racecdn/media/' + str(t)                                                                                                
    count = count+1                                                                                                                           
    try:                  
        print(count)                                                                                                                         
        f = MP3(fp)                                                                                                                        
        fbr=int(f.info.bitrate/1000)                                                                                                              
        print(fbr)                                                                                                                 
        if fbr > 128 and fp.endswith('.mp3'):                                                                                      
           btrs.append(fp)                                                                 
        elif fbr < 192 and fp.endswith('.mp3'):                      
           strs.append(fp)                                                                                         
   #pass                                                                                                                       
    except:                                                                                                                        
        pass                 


###### rename script

import os
import sys
directory='/racecdn/media/tracks/low/'
#directory = os.path.dirname(os.path.realpath(sys.argv[0])) #get the directory of your script
for subdir, dirs, files in os.walk(directory):
 for filename in files:
  if filename.find('.mp3') > 0:
   subdirectoryPath = os.path.relpath(subdir, directory) #get the path to your subdirectory
   filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
   newFilePath = fil
   ePath.replace("128.mp3","low.mp3") #create the new name
   os.rename(filePath, newFilePath) #rename your file
###############################################################



import os
from mutagen.mp3 import MP3

txs = Track.objects.all()
err= []

for tx in txs:
    filepath = '/racecdn/media/' + str(tx.original)
    try:

        file_info = MP3(filepath)
    except HeaderNotFoundError as err:
        try:
            print(err)
            file_info.pprint()
            file_bitrate = int(file_info.info.bitrate/1000)
            print(str(tx.original),"   ID=", tx.id)
            
                if file_bitrate > 127 and filepath.endswith('.mp3'):


                    print(filepath)
                    print(file_bitrate)

                    songname = filepath.rsplit('/',1)[1][:-4]

                    if file_bitrate > 127 and filepath.endswith('.mp3'):
                        base_low = '/racecdn/media/tracks/low/'
                        new_file_name_low = base_low + songname + '_low' + '.mp3'
                        my_cmd_low = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 128k ' + new_file_name_low

                        if os.path.exists(new_file_name_low) is not True:
                            os.system(my_cmd==ow)
                            print(new_file_name_low+" converted 128")

                    if file_bitrate > 191 and filepath.endswith('.mp3'):
                        base_medium = '/racecdn/media/tracks/medium/'
                        new_file_name_medium = base_medium + songname + '_medium' + '.mp3'
                        my_cmd_medium = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 192k ' + new_file_name_medium

                        if os.path.exists(new_file_name_medium) is not True:
                            os.system(my_cmd==edium +" converted 192")
                            print(new_file_name_medium)

                    if file_bitrate > 319 and filepath.endswith('.mp3'):
                        new_file_name_high = base_medium + songname + '_high' + '.mp3'
                        if file_bitrate == 320:

                            if os.path.exists(new_file_name_high) is not True:
                                copyfile(filepat==new_file_name_high)
            
                        else:
                            base_high = '/racecdn/media/tracks/high/'
                            new_file_name_high = base_high + songname + '_high' + '.mp3'
                            my_cmd_high = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 320k ' + new_file_name_high

                        
            #except Exception as err:
            #print(err)
            
            except HeaderNotFoundError as err:

                print(err)
                print('-----------------------')
    #######################
    if mp3:
        if bitrate=128 and new_file_name_low not exist:
            copy
        if bitrate > 128 and new_file_name_low not exist:
            convert
        if bitrate = 192 and new_file_name_medium not exist:
            copy
        if bitrate > 192 and new_file_name_medium not exist:
            convert
        if bitrate =320 and new_file_name_high not exist:
            copy
        if bitrate >320 and new_file_name_high not exist:
            convert



##############################################################c###

import os
from mutagen.mp3 import MP3
from shutil import copyfile
object_id_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/error-songs.txt')]
txs = Track.objects.all().order_by('id').filter(id__gte=23519).exclude(id__in=object_id_list)

for tx in txs:
    filepath = '/racecdn/media/' + str(tx.original)

    if filepath.endswith('.mp3'):

        file_info = MP3(filepath)
        file_bitrate = int(file_info.info.bitrate/1000)

        print(tx.id)
        print(filepath)
        print(file_bitrate)

        songname = filepath.rsplit('/',1)[1][:-4]

        if file_bitrate > 127:
            base_low = '/racecdn/media/tracks/low/'
            new_file_name_low = base_low + songname + '_low' + '.mp3'
            new_loc_low = 'tracks/low/' + songname + '_low' + '.mp3'
            my_cmd_low = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 128k ' + new_file_name_low

            if os.path.exists(new_file_name_low) is not True:
                if file_bitrate == 128:
                    copyfile(filepath, new_file_name_low)
                    print(new_file_name_low)
                else:    
                    os.system(my_cmd_low)
                    print(new_file_name_low)

            tx.media_low = new_loc_low

        if file_bitrate > 191:
            base_medium = '/racecdn/media/tracks/medium/'
            new_file_name_medium = base_medium + songname + '_medium' + '.mp3'
            new_loc_medium = 'tracks/medium/' + songname + '_medium' + '.mp3'
            my_cmd_medium = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 192k ' + new_file_name_medium

            if os.path.exists(new_file_name_medium) is not True:
                if file_bitrate == 192:
                    copyfile(filepath, new_file_name_medium)
                    print(new_file_name_medium)
                else:    
                    os.system(my_cmd_medium)
                    print(new_file_name_medium)

            tx.media_medium = new_loc_medium

        if file_bitrate > 319:
            base_high = '/racecdn/media/tracks/high/'
            new_file_name_high = base_high + songname + '_high' + '.mp3'
            new_loc_high = 'tracks/high/' + songname + '_high' + '.mp3'
            my_cmd_high = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 320k ' + new_file_name_high

            if os.path.exists(new_file_name_high) is not True:
                if file_bitrate == 320:
                    copyfile(filepath, new_file_name_high)
                    print(new_file_name_high)
                else:    
                    os.system(my_cmd_high)
                    print(new_file_name_high)

            tx.media_high = new_loc_high

#        tx.save()
        print('-----------------------')




###################################

#####################################################################3


## MP3 conversion integrity checker

import os
from mutagen.mp3 import MP3
from shutil import copyfile

object_id_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/error-songs.txt')]
txs = Track.objects.all().order_by('id').exclude(id__in=object_id_list)

for tx in txs:
    filepath = '/racecdn/media/' + str(tx.original)

    if filepath.endswith('.mp3'):

        file_info = MP3(filepath)
        file_bitrate = int(file_info.info.bitrate/1000)

        print(tx.id)
        print(filepath)
        print(file_bitrate)

        songname = filepath.rsplit('/',1)[1][:-4]

        if file_bitrate > 127:
            base_low = '/racecdn/media/tracks/low/'
            new_file_name_low = base_low + songname + '_low' + '.mp3'
            new_loc_low = 'tracks/low/' + songname + '_low' + '.mp3'
            my_cmd_low = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 128k ' + new_file_name_low

            if os.path.isfile(new_file_name_low) is True:
                
                try:
                    br = int(MP3(new_file_name_low).info.bitrate/1000)
                except:
                    if file_bitrate == 128:
                        copyfile(filepath, new_file_name_low)
                    else:
                        os.system(my_cmd_low)

                tx.media_low = new_loc_low

            else:
                tx.media_low = ''
        
        else:
            tx.media_low = ''



            

        if file_bitrate > 191:
            base_medium = '/racecdn/media/tracks/medium/'
            new_file_name_medium = base_medium + songname + '_medium' + '.mp3'
            new_loc_medium = 'tracks/medium/' + songname + '_medium' + '.mp3'
            my_cmd_medium = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 192k ' + new_file_name_medium

            
            if os.path.isfile(new_file_name_medium) is True:
                
                try:
                    br = int(MP3(new_file_name_medium).info.bitrate/1000)
                except:
                    if file_bitrate == 192:
                        copyfile(filepath, new_file_name_medium)
                    else:
                        os.system(my_cmd_medium)

                tx.media_medium = new_loc_medium

            else:
                if file_bitrate == 192:
                    copyfile(filepath, new_file_name_medium)
                else:    
                    os.system(my_cmd_medium)

                tx.media_medium = ''

            tx.media_medium = new_loc_medium
        
        else:
            tx.media_medium = ''





        if file_bitrate > 319:
            base_high = '/racecdn/media/tracks/high/'
            new_file_name_high = base_high + songname + '_high' + '.mp3'
            new_loc_high = 'tracks/high/' + songname + '_high' + '.mp3'
            my_cmd_high = 'ffmpeg -y -i ' + filepath +' -codec:a libmp3lame -b:a 320k ' + new_file_name_high

            if os.path.isfile(new_file_name_high) is True:

                try:
                    br = int(MP3(new_file_name_high).info.bitrate/1000)
                except:
                    if file_bitrate == 320:
                        copyfile(filepath, new_file_name_high)
                    else:
                        os.system(my_cmd_high)

                tx.media_high = new_loc_high
                
            else:
                tx.media_high = ''
        else:
            tx.media_high = ''

        tx.save()
        print('-----------------------')