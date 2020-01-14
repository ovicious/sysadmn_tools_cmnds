
#!/usr/bin/python

import os
#ssudoPassword = '45963214'
#command = 'mount -t vboxsf myfolder /home/myuser/myfolder'
#os.system('cd /racecdn')
#os.system('pwd')
os.system('echo 45963214 | sudo -S chown -R avishek:www-data /racecdn/media/*')
os.system('echo 45963214 | sudo -S chmod -R 775 /racecdn/media/*')
#p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
#os.popen("sudo -S %s"%(command), 'w').write('mypass')