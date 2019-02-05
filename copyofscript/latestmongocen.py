from fabric.api import *
userr=raw_input("Enter Username:")
env.user = userr
lorl=raw_input("Local[1] Live[2]:\n")
if lorl == '1':
  env.password = ""
elif lorl == '2' :
  file=raw_input("Pem name:")
  env.key_filename = '/home/ndot/logirocker/pem/'+file+'.pem'
else :
  print("Sorry:")
  exit()
def mongo():
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
mongo()
