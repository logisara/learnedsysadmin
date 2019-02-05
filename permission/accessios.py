from fabric.api import *
env.user='macadmin'
env.password='rAnGErs@S%s@dm!'
def github():
	put('/home/ndot/Desktop/Host/hosts','/tmp')
	sudo('mv /tmp/hosts /etc/hosts')
def facebook():
        put('/home/ndot/Desktop/Host/hostsfb','/tmp')
	sudo('mv /tmp/hostsfb /etc/hosts')
def youtube():
	put('/home/ndot/Desktop/Host/hostsyou','/tmp')
	sudo('mv /tmp/hostsyou /etc/hosts')
def BDE():
	put('/home/ndot/Desktop/Host/hostsbd','/tmp')
        sudo('mv /tmp/hostsbd /etc/hosts')
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
