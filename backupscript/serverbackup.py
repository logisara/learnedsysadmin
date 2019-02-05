from fabric.api import *
env.user='root'
env.password='D@nGerOut18!'

print "********!!**Welcome to Backup Process**!!*********"
Date=raw_input('\n\nDate:')

def mongo():
  env.password='D@nGer0ut18!'
  def func():
    run('zip -r MongoBackup'+Date+'.zip .')
    get('/root/Backup/MongoBackup'+Date+'.zip', '/mnt/Mongo/')
    run('rm -rf MongoBackup'+Date+'.zip')


  with cd('/root/'):
    #run('ls -a')
    #run('sh mongo.sh')
    with cd('/root/Backup/'):
        run('ls')
        run('df -h')
        choice = raw_input("\n How Many Days Backup delete 1,2 or 3:")

        if choice == '1':
         i1 = raw_input("date:")
         run('rm -rf ' + i1 + ' ')
         func()
        elif choice == '2':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         run(' rm -rf ' + i1 + ' ' + i2 + '')
         func()
        elif choice == '3':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         i3 = raw_input("date2:")
         run('rm -rf ' + i1 + ' ' + i2 + ' ' + i3 + '')
         func()
        elif choice == 'n':
         func()
        else:
          print("\n nothing to do")
#--------------------------------------------------------------------------------------------------------------------------#
def share():
	env.password='D@nGer0ut18!'
	with cd('/home/Samba/'):
	 run('df -h')
         run('zip -r HRD'+Date+'.zip HRD')
         run('zip -r HRD_DOCS'+Date+'.zip HRD_DOCS')
         get('/home/Samba/HRD'+Date+'.zip', '/mnt/samba/HRD/')
         get('/home/Samba/HRD_DOCS'+Date+'.zip' , '/mnt/samba/HRD/')
         run('rm -rf HRD_DOCS'+Date+'.zip')
         run('rm -rf HRD'+Date+'.zip')
         with cd ('/home/Samba/Finance/'):
          run('zip -r Finance'+Date+'.zip .')
          get('/home/Samba/Finance/Finance'+Date+'.zip','/mnt/samba/Finance')
          run('rm -rf Finance'+Date+'.zip')
#-------------------------------------------------------------------------------------------------------------#
def OwayDb():
    env.password='D@nGer0ut18!'
    def func():
     with cd('/root/DBBACKUP/'):
      run('zip -r '+Date+'.zip .')
      get('/root/DBBACKUP/'+Date+'.zip', '/mnt/DB/OWAY/')
      run('rm -rf '+Date+'.zip')

    #with cd('/root/'):
    #run('ls -a')
    #run('sh mongo.sh')
    with cd('/root/DBBACKUP/'):
        run('ls')
        run('df -h')
        choice = raw_input("\n How Many Days Need to delete 1,2 or 3:")

        if choice == '1':
         i1 = raw_input("date:")
         run('rm -rf ' + i1 + ' ')
         func()
        elif choice == '2':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         run(' rm -rf ' + i1 + ' ' + i2 + '')
         func()
        elif choice == '3':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         i3 = raw_input("date2:")
         run('rm -rf ' + i1 + ' ' + i2 + ' ' + i3 + '')
         func()
        elif choice == 'n':
         func()
        else:
          print("\n nothing to do")
#------------------------------------------------------------------------------------------------------------------------#
def Localmysql():
    env.password='D@nGer0ut18!'
    def func():
     run('zip -r MysqlBackup'+Date+'.zip .')
     get('/root/Backup/Mysql/MysqlBackup'+Date+'.zip', '/mnt/DB/Mysql1/')
     run('rm -rf MysqlBackup'+Date+'.zip')
    #with cd('/root/'):
    with cd('/root/Backup/Mysql/'):
        run('ls')
        run('df -h')
        choice = raw_input("\n How Many Days need to Delete 1,2 or 3:")

        if choice == '1':
         i1 = raw_input("date:")
         run('rm -rf ' + i1 + ' ')
         func()
        elif choice == '2':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         run(' rm -rf ' + i1 + ' ' + i2 + '')
         func()
        elif choice == '3':
         i1 = raw_input("date:")
         i2 = raw_input("date1:")
         i3 = raw_input("date2:")
         run('rm -rf ' + i1 + ' ' + i2 + ' ' + i3 + '')
         func()
        elif choice == 'n':
         func()
        else:
          print("\n nothing to do")
#--------------------------------------------------------------------------------------------------------------------------#
def svnDbbackup():
 env.password='D@nGer0ut18!'
 with cd('/opt/'):
  try:
    run('mysqldump -f -u root -p --all-databases --skip-lock-tables > alldbSVN'+Date+'.sql')
    get('/opt/alldbSVN.sql' , '/mnt/DB/03/')
  except:
    get('/opt/alldbSVN'+Date+'.sql' , '/mnt/DB/SVN3/')
#---------------------------------------------------------------------------------------------------------------------------#
def main():
	
	 print "\n\n--** Select numbers to get Backup of specific server **--"
	 print("\nRegular Backup...!!")

         ver = raw_input("\n3.22[1] \nHRD & FINANCE[2]")

	 print("\nWeekly Backup ..!!")
	 ver = raw_input("\n3.79[3] \n3.97[4] \n3.243db[5] \n\nQuit[q]:")
	 if ver == '1':
		mongo()
		main()
	 if ver == '2':
		share()
		main()
	 if ver =='3':
		OwayDb()
		main()
	 if ver == '4':
		Localmysql()
		main()
	 if ver == '5':
		svnDbbackup()
		main()

main()
