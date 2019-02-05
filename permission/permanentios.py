from fabric.api import *
env.user='macadmin'
env.password='rAnGers@Sysadm'
def github():
	put('/home/ndot/Desktop/Host/hosts','/tmp')
	sudo('cp -rf /tmp/hosts /etc/hosts')
	sudo('mv /tmp/hosts /etc/apache2/hosts')
def facebook():
        put('/home/ndot/Desktop/Host/hostsfb','/tmp')
	sudo('cp /tmp/hostsfb /etc/hosts')
	sudo('mv /tmp/hostsfb /etc/apache2/hosts')
def youtube():
	put('/home/ndot/Desktop/Host/hostsyou','/tmp')
	sudo('cp /tmp/hostsyou /etc/hosts')
	sudo('mv /tmp/hostsyou /etc/apache2/hosts')

def BDE():
	put('/home/ndot/Desktop/Host/hostsbd','/tmp')
        sudo('cp /tmp/hostsbd /etc/hosts')
	sudo('mv /tmp/hostsbd /etc/apache2/hosts')
def main():
	ver=raw_input('\ngithub[1] \nfacebook[2] \nyoutube[3] \nBDE[4] \nQuit[5]:')
	if ver == '1':
	  github()
          main()
	if ver == '2':
	  facebook()
	  main()
	if ver == '3':
	  youtube()
	  main()
	if ver == '4':
	  BDE()
	  main()
	else:
	 exit()
main()
