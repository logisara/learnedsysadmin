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
def browser():
	 put('/home/ndot/Downloads/google-chrome-stable_current_amd64.deb','/tmp')
	 with cd("/tmp"):
          sudo('dpkg -i google-chrome-stable_current_amd64.deb')
	  try:
	   sudo('apt-get update')
	  #sudo('dpkg -i google-chrome-stable_current_amd64.deb')
	  #sudo('dpkg -i google-chrome-stable_current_amd64.deb')
	   sudo('apt-get install firefox')
	  except:
		sudo('apt-get install firefox')
def node():
	    ch=raw_input("Is Node Already installed?[Y/n]:")
	    if ch == 'y' or ch == 'Y':
  	     try:
 #run("n "+ver)
   	        ver=raw_input("Enter Version:")
   		sudo("n "+ver)
  	     except:
    		exit()
def php():
            sudo('add-apt-repository ppa:ondrej/php')
            try:
              sudo('apt-get update')
              sudo('apt-get install -y php7.2 libapache2-mod-php7.2 php7.2-cli php7.2-common php7.2-mbstring php7.2-gd php7.2-mysql php7.2-zip')
              sudo('a2dismod php7.0')
	      sudo('a2enmod php7.2')
	      sudo('service apache2 restart')
	    except:
	      sudo('apt-get install -y php7.2 libapache2-mod-php7.2 php7.2-cli php7.2-common php7.2-mbstring php7.2-gd php7.2-mysql php7.2-zip')
              sudo('a2dismod php7.0')
              sudo('a2enmod php7.2')
	      sudo('service apache2 restart')
def mongo():
	    pver=raw_input("Mongo Particular Version[4.0 or 4.1]:")
	    ver=raw_input("Version[4.0 or 4.1]:")
            sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-mongos_'+pver+'_amd64.deb')
            sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-server_'+pver+'_amd64.deb')
            sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-shell_'+pver+'_amd64.deb')
            sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org-tools_'+pver+'_amd64.deb')
            sudo('wget http://repo.mongodb.org/apt/ubuntu/dists/xenial/mongodb-org/'+ver+'/multiverse/binary-amd64/mongodb-org_'+pver+'_amd64.deb')
            try:
             sudo('dpkg -i mongodb-org*')
	     sudo('systemctl daemon-reload')
             sudo('systemctl start mongod')
             sudo('systemctl enable mongod')
	     sudo('service mongod status')
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

def mongocen():
	    pver=raw_input("Mongo Particular Version[4.0 or 4.1]:")
            ver=raw_input("Version[4.0 or 4.1]:")
            sudo('wget http://repo.mongodb.org/yum/redhat/7Server/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-'+pver+'-1.el7.x86_64.rpm')
            sudo('wget http://repo.mongodb.org/yum/redhat/7Server/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-mongos-'+pver+'-1.el7.x86_64.rpm')
            sudo('wget http://repo.mongodb.org/yum/redhat/7Server/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-server-'+pver+'-1.el7.x86_64.rpm')
            sudo('wget http://repo.mongodb.org/yum/redhat/7Server/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-shell-'+pver+'-1.el7.x86_64.rpm')
            sudo('wget http://repo.mongodb.org/yum/redhat/7Server/mongodb-org/'+ver+'/x86_64/RPMS/mongodb-org-tools-'+pver+'-1.el7.x86_64.rpm')
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
            if key == 'y' or key == 'Y':
                sudo('rm -rf mongodb-org*')
            else:
                print("Saved")

def main():
    ver = raw_input("\nBroswer[1] \nNode[2] \nphp[3] \nmongo[4] \nmongocentos[5] \nphp-mongodb[6] \nQuit[q]:")
    if ver =='1':
	browser()
	main()
    elif ver =='2':
	node()
	main()
    elif ver =='3':
	php()
	main()
    elif ver =='4':
	mongo()
	ini()
	main()
    elif ver == '5':
	mongocen()
	main()
    elif ver == '6':
	ini()
	main()
    else:
	print("Nothing to do")
	exit()
main()
   

