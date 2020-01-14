    import os
    from mutagen.mp3 import MP3
    from shutil import copyfile
    object_id_list=[line.rstrip('\n') for line in open('/tmp/imagine-works/error-songs.txt')]
    txs = Track.objects.all().order_by('id').filter(id__gte=130001).filter(id__lte=150000).exclude(id__in=object_id_list)

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

            tx.save()
            print('-----------------------')


