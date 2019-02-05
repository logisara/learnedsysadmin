from fabric.api import *
import os
env.user = 'root'
env.password = 'rAnGers@Sysadm'
Date = raw_input("Date:")
with cd('/usr/local/src/'):
     run('df -h')
     run('ls')
     var = raw_input("continue[Y/n]:")
     if var =='y' or var == 'Y':
      run('df -h')
      run('ls')
      #run('du -sh')
      run('zip -r ubersvn'+Date+'.zip ubersvn')
      run('mv ubersvn'+Date+'.zip /var/www/html')
      os.system('wget http://192.168.1.243/ubersvn'+Date+'.zip')
      os.system('sudo mv ubersvn'+Date+'.zip /mnt/SVN1/OLD/')
      run('rm -rf ubersvn'+Date+'.zip')
