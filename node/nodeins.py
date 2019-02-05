from fabric.api import *
userr = raw_input("Enter Username:")
env.user = userr
env.password = "Sy$Adm#Cl0ud18"
#try:
#run("node -v")
ch=raw_input("Is Node Already installed?[Y/n]:")
if ch == 'y' or ch == 'Y':
  try:
 #run("n "+ver)
   ver=raw_input("Enter Version:")
   sudo("n "+ver)
  except:
    exit()
else:
     def one():
	try:
	    try:
	      sudo("apt-get update")
	      sudo('apt-get install npm')
  	      sudo('npm install n -g')
  	      sudo('n '+ver)
  	      run("node -v")
  	      run("npm -v")	
	    except:
	      sudo('apt-get install npm')
  	      sudo('npm install n -g')
  	      sudo('n '+ver)
  	      run("node -v")
  	      run("npm -v")
  	except:
  	  alt=raw_input("Enter Alternative command:")
  	  sudo(alt)
     one()
