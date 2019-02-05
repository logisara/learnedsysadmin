from fabric.api import *

env.user = 'ndot'
#env.host = '192.168.2.32'
env.password = 'rAnGErs@S%s@dm!'
def one():
   put('/etc/rc.local', '/tmp')
   sudo('mv /etc/rc.local /home/ndot/Desktop/rc.local.bk')
   sudo('mv /tmp/rc.local /etc/')
one()

