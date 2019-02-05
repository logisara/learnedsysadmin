from fabric.api import *
env.user='hduser'
env.passwd='ndot'
env.hosts=['192.168.3.56','192.168.3.59']
def harddisk():
    sudo('apt-get install smartmontools')
    sudo('fisk -l')
    a=ram_input("a:")
    sudo('smartctl -H /dev/sda'+a)
harddisk()
