from fabric.api import *
env.user="ndot"
env.password="rAnGErs@S%s@dm!"
def github():
	put('/home/ndot/Desktop/Host/hosts','/tmp')
	sudo('mv /tmp/hosts /etc/hosts')
	sudo('service cron stop')
def facebook():
        put('/home/ndot/Desktop/Host/hostsfb','/tmp')
	sudo('mv /tmp/hostsfb /etc/hosts')
	sudo('service cron stop')
def youtube():
	put('/home/ndot/Desktop/Host/hostsyou','/tmp')
	sudo('mv /tmp/hostsyou /etc/hosts')
	sudo('service cron stop')
def BDE():
	put('/home/ndot/Desktop/Host/hostsbd','/tmp')
        sudo('mv /tmp/hostsbd /etc/hosts')
	sudo('service cron stop')
def flipkart():
	put('/home/ndot/Desktop/Host/hostsfp','/tmp')
        sudo('mv /tmp/hostsfp /etc/hosts')
def main():
	ver=raw_input('\ngithub[1] \nfacebook[2] \nyoutube[3] \nBDE[4] \nFlipkart[5] \nQuit[6]:')
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
	if ver == '5':
	  flipkart()
	  main()
	else:
	 exit()
main()
