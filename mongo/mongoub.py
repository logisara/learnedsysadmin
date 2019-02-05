from fabric.api import *
userr=raw_input("Enter Username:")
env.user = userr
lorl=raw_input("Local[1] Live[2]:\n")
if lorl == '1':
	env.password = ''
elif lorl == '2' :
	file=raw_input("Pem name:")
	env.key_filename = '/home/ndot/'+file+'.pem'
else :
 	print("Sorry:")
 	exit()	
def unstab():
	pver=raw_input("Particular Version[3.x.x or 4.x.x]:")
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-unstable-mongos_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-unstable-server_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-unstable-shell_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-unstable-tools_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-unstable_'+pver+'_amd64.deb')
	try:
	  sudo('dpkg -i mongodb-org-unstable*')
	  sudo('service mongod restart')
	  sudo('service mongod status')
	except:
            alt=raw_input("Alternative command:")
	    sudo(alt)
	key=raw_input('Need to remove the .Deb File[y/n]:')
	if key == 'y' or key == 'Y':
		sudo('rm -rf mongodb-org*')
	else:
		print("Saved")
def install():
	pver=raw_input("Particular Version[3.x.x or 4.x.x]:")
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-mongos_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-server_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-shell_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-tools_'+pver+'_amd64.deb')
	sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org_'+pver+'_amd64.deb')
	try:
		  sudo('dpkg -i mongodb-org*')
	  	  try:
                    sudo('systemctl daemon-reload')
                    sudo('systemctl start mongod')
                    sudo('systemctl enable mongod')
                    sudo('service mongod status')
   	  	    #sudo('service mongod restart')
	  	    #sudo('service mongod status') 
	  	  except:
                    sudo('systemctl daemon-reload')
                    sudo('systemctl start mongod')
                    sudo('systemctl enable mongod')
                    sudo('service mongod status')
	  	    #sudo('service mongodb restart')
	  	    #sudo('service mongodb status')
	except:
		try:
		    sudo('apt-get install libcurl3')
		    try:
			    sudo('service mongod restart')
			    sudo('service mongod status') 
		    except:
			    sudo('service mongodb restart')
			    sudo('service mongodb status')
	  	except:
           		alt=raw_input("Alternative command:")
	    		sudo(alt)
	key=raw_input('Need to remove the .Deb File[y/n]:')
	if key == 'y' or key == 'Y':
		sudo('rm -rf mongodb-org*')
	else:
		print("Saved")
def ini():
	print("connecting mongodb....")
	sudo("php -v")
	version=raw_input("PHP Version:")
	sudo("apt-get install php-mongodb")
	sudo('sed -i 1916iextension=mongodb.so /etc/php/'+version+'/apache2/php.ini')
	sudo("service apache2 restart")

#Main program
print("Note:versin=3.2 to 4.1")
ver=raw_input("Version[3.4 or 4.1]:")
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
       print("Note:3.6 to 3.6.10")
       install()
elif ver == '4.0':
       print("Note:4.0 to 4.0.5")
       install()
elif ver == '4.1':
       print("Note:4.1 to 4.1.7")
       unstab()
else:
	print("Sorry!")

func = raw_input("Need to connect Mongodb-php[y/n]:")
if func == 'y' or func == 'Y':
					ini()
elif func == 'n' or  func == 'N':
	 print("Thank You!!")
 	 exit()
else:
	exit()
