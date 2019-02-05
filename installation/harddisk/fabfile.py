from fabric.api import *
env.user='ndot'
env.hosts=['192.168.1.73','192.168.1.83','192.168.1.45','192.168.1.217','192.168.1.155','192.168.1.211','192.168.2.39','192.168.2.81']
env.password='rAnGErs@S%s@dm!'
def harddisk():
     try:
      sudo('apt-get update')
      sudo('apt-get -y install smartmontools')
      sudo('fdisk -l')
      sudo('smartctl -H /dev/sda')
     except:
      sudo('apt-get -y install smartmontools')
      sudo('apt-get -y install smartmontools')
      sudo('fdisk -l')
      sudo('smartctl -H /dev/sda')


    

