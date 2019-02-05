from fabric.api import *
userr=raw_input("Enter Username:")
env.user = userr
lorl=raw_input("Local[1] Live[2]:\n")
if lorl == '1':
	env.password = ''
elif lorl == '2' :
	file=raw_input("Pem name:")
	env.key_filename = '/home/ndot/logirocker/pem/'+file+'.pem'
else :
 	print("Sorry:")
 	exit()	
def unstab():
	pver=raw_input("Particular Version[3.x.x or 4.x.x]:")
        #run('cat /etc/redhat-release')
	osver=raw_input("OS version[5,6,7]:")
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-unstable'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-unstable-mongos-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-unstable-server-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-unstable-shell-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-unstable-tools-'+pver+'-1.el'+osver+'.x86_64.rpm')

        try:
          sudo('rpm -i mongodb-org*')
          sudo('systemctl daemon-reload')
          sudo('systemctl start mongod')
          sudo('systemctl enable mongod')
          sudo('service mongod status')
	except:
            alt=raw_input("Alternative command:")
	    sudo(alt)
	key=raw_input('Need to remove the .rpm File[y/n]:')
	if key == 'y':
		sudo('rm -rf mongodb-org-*')
	else:
		get=run("pwd")
		print("Saved in"+get)
def install():
	pver=raw_input("Particular Version[3.x.x or 4.x.x]:")
        run('cat /etc/redhat-release')
	osver=raw_input("OS version[5,6,7]:")
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-mongos-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-server-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-shell-'+pver+'-1.el'+osver+'.x86_64.rpm')
	sudo('wget https://repo.mongodb.org/yum/redhat/'+osver+'/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-tools-'+pver+'-1.el'+osver+'.x86_64.rpm')
	try:
          sudo('yum install openssl')
	  sudo('rpm -i mongodb-org*')
          sudo('systemctl daemon-reload')
          sudo('systemctl start mongod')
          sudo('systemctl enable mongod')
	  sudo('service mongod status')
	except:
            alt=raw_input("Alternative command:")
	    sudo(alt)
	key=raw_input('Need to remove the .rpm File[y/n]:')
	if key == 'y':
		sudo('rm -rf mongodb-org-*')
	else:
		get=run("pwd")
		print("Saved in"+get)
def ini():
	print("connecting mongodb....")
	sudo("yum install pecl")
	sudo("pecl install mongodb")
	sudo('sed -i 1916iextension=mongodb.so /etc/php.ini')
	sudo("service httpd restart")
        sudo("pecl search mongo")
#Main program
print("Note:versin=3.2 to 4.0")
ver=raw_input("Version[3.4 or etc]:")
if ver == '3.2':
	print("Note:3.2.7 to 3.2.16")
	install()
elif ver == '3.3':
	print("Note:3.3.7 to 3.3.15")
	con=raw_input("This is an Unstable Version[y/n]:")
	if con == 'y' or con == 'Y':
		unstab()
elif ver == '3.4':
	print("Note:3.4.0 to 3.4.7")
	install()
elif ver == '3.5':
	print("Note:3.5.1 to 3.4.12")
	con=raw_input("This is an Unstable Version[y/n]:")
	if con == 'y' or con == 'Y':
		unstab()
elif ver == '3.6':
        print("Note:3.6.1 to 3.6.4")
        install()
elif ver == '4.0':
        print("Note:4.0.0 to 4.0.5")
        install()

else:
	print("Sorry!")

fun = raw_input("Need to connect Mongodb-php[y/n]:")
if fun == 'y' or fun == 'Y':
	ini()
else:
	print("Thank you!")
	exit()
