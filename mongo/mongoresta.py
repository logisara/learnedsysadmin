from fabric.api import *
env.user = 'ndot'
env.password = 'rAnGErs@S%s@dm!'
env.hosts=['logesh']
try:
   sudo('service mongod restart')
   sudo('service mongod status')
except:
   sudo('service mongodb restart')
   sudo('service mongodb status')

