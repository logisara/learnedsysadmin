from fabric.api import *
env.user='ndot'
env.password='rAnGErs@S%s@dm!'
def github():
        put('/home/ndot/Desktop/Host/hoststicket','/tmp')
        sudo('mv /tmp/hoststicket /etc/hosts')
        #sudo('service cron stop')
	sudo('cp -rf /etc/hosts /usr/local/hosts')
github()

