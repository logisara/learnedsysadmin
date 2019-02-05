from fabric.api import *
userr=raw_input("Enter Username:")
env.user = userr
lorl=raw_input("Local[1] Live[2]:\n")
if lorl == '1':
    env.password = ''
elif lorl == '2' :
    file=raw_input("Pem name:")
    env.key_filename = '/home/ndot/'+file+'.pem'
else :
    print("Sorry:")
    exit()

ver=raw_input("Enter Version:")
def one():
	try:
	  	sudo('sudo yum install epel-release')
  	 	sudo('yum install npm')
                sudo('npm install n -g')
  	        sudo('n '+ver)
  	  	run("node -v")
  	  	run("npm -v")
  	except:
  	  alt=raw_input("Enter Alternative command:")
  	  run(alt)
one()
