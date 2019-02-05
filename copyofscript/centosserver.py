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
def func():
	sudo('yum install wget tar')
	sudo('yum install httpd')
	sudo('service httpd start')
	sudo('yum install zip unzip openssl openssl-devel')
	sudo('yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
	sudo('yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm')
	sudo('yum install yum-utils')
	php_version=raw_input('php_version input as 0 or 1 or 2:')
	sudo('yum-config-manager --enable remi-php7'+php_version)
	sudo('yum install php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo')
	sudo('yum -y install gcc php-pear php-devel')
	sudo('php -v')
	sudo('wget http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz')
	sudo('tar -xvf ioncube_loaders_lin_x86-64.tar.gz')
	sudo('cp ioncube/ioncube_loader_lin_7.'+php_version+'.so /usr/lib64/php/modules/')
        sudo('sed -i 1637izend_extension = /usr/lib64/php/modules/ioncube_loader_lin_7.'+php_version+'.so /etc/php.ini')
func()

