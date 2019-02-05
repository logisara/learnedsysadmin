from fabric.api import *
userr=raw_input("Enter Username:")
env.user = userr
lorl=raw_input("Local[1] Live[2]:\n")
if lorl == '1':
  env.password = 'ndot'
elif lorl == '2' :
  file=raw_input("Pem name:")
  env.key_filename = '/home/ndot/'+file+'.pem'
else :
  print("Sorry:")
  exit()  

def google_chrome():
     ch=raw_input("Is google-chrome Already installed?[Y/n]:")
     if ch == 'y' or ch == 'Y':
        sudo('apt-get purge google-chrome*')
        run('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
        sudo('echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list')
        try:
         sudo('apt-get update')
         sudo('apt-get install google-chrome-stable')
        except:
         sudo('apt-get install google-chrome-stable')

     else:
        run('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
        sudo('echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list')
        try:
         sudo('apt-get update')
         sudo('apt-get install google-chrome-stable')
        except:
         sudo('apt-get install google-chrome-stable')

def chromium():
     ch=raw_input("Is chromium-browser Already installed?[Y/n]:")
     if ch == 'y' or ch == 'Y':
        sudo('apt-get purge chromium-browser')
        try:
         sudo('apt-get update')
         sudo('apt-get install chromium-browser')

        except:
         sudo('apt-get install chromium-browser')
     else:
        try:
         sudo('apt-get update')
         sudo('apt-get install chromium-browser')

        except:
         sudo('apt-get install chromium-browser')

def firefox():
     ch=raw_input("Is firefox Already installed?[Y/n]:")
     if ch == 'y' or ch == 'Y':
        sudo('apt-get purge firefox')
        try:
         sudo('apt-get update')
         sudo('apt-get install firefox')
        except:
         sudo('apt-get install firefox')
     else:  
       try:
         sudo('apt-get update')
         sudo('apt-get install firefox')
       except:
         sudo('apt-get install firefox')

def filezilla():
       try:
         sudo('apt-get update')
         sudo('apt-get install filezilla')
       except:
         sudo('apt-get install filezilla')

def skype():
      run('wget https://go.skype.com/skypeforlinux-64.deb')
      try:
        sudo('sudo apt-get update')
        sudo('dpkg -i skypeforlinux-64.deb')
      except:
        sudo('dpkg -i skypeforlinux-64.deb')
      run("rm -rf skypeforlinux*")

def robo():
      run('wget https://download.robomongo.org/1.1.1/linux/robo3t-1.1.1-linux-x86_64-c93c6b0.tar.gz')
      run("tar -xvzf robo3t-1.1.1-linux-x86_64-c93c6b0.tar.gz")
      sudo("mv robo3t-1.1.1-linux-x86_64-c93c6b0/ /home/developer/Desktop/robo3t")
      sudo("chown -R developer:developer /home/developer/Desktop/robo3t")
      sudo("chmod -R 777 /home/developer/Desktop/robo3t")
def lamp():
      try:
        sudo('apt-get update')
        sudo('apt-get install apache2')
        sudo('apt-get install mysql-client')
        sudo('apt-get install php7.0')
      except:
        sudo('apt-get install apache2')
        sudo('apt-get install mysql-client')
        sudo('apt-get install php7.0')
def andr():
      run('sudo add-apt-repository ppa:maarten-fonville/android-studio')
      try:  
         sudo('apt-get update')
         sudo('apt install android-studio')
      except:
         sudo('apt install android-studio')
def sublime():
	run('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
	sudo('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
	try:
  	  sudo('apt-get update')
	  sudo('apt-get install sublime-text')	
	except:
  	  sudo('apt-get install sublime-text')

def eclipse():
      
      try:  
         sudo('apt-get update')
         sudo('apt-get install eclipse')
      except:
         sudo('apt-get install eclipse')
def two():
     env.host =""
     env.user ="ndot"
     env.password="ndot"
     def one():
       sudo('chmod -R 000 /media/')
       sudo('chmod -R 000 /mnt/')
       try:
        #sudo('sudo chmod 000 /usr/bin/teamviewer')
        #sudo('sudo chmod 000 /usr/bin/vlc')
        put('/home/ndot/Desktop/hosts', '/tmp')
        sudo('cp -rf /etc/hosts /home/ndot')
        sudo('cp -rf /tmp/hosts /etc/')
        sudo('cp -rf /tmp/hosts /usr/local/')
        sudo('cp -rf /etc/crontab /home/ndot')
        put('/home/ndot/Desktop/crontab', '/tmp')
        sudo('cp -rf /tmp/crontab /etc/')
        sudo('useradd developer')
        sudo('passwd developer')
        put('/home/ndot/Desktop/itacl', '/home/ndot/')
        sudo('passwd ndot')
       except:
        put('/home/ndot/Desktop/hosts', '/tmp')
        sudo('cp -rf /etc/hosts /home/ndot')
        sudo('cp -rf /tmp/hosts /etc/')
        sudo('cp -rf /tmp/hosts /usr/local/')
        sudo('cp -rf /etc/crontab /home/ndot')
        put('/home/ndot/Desktop/crontab', '/tmp')
        sudo('cp -rf /tmp/crontab /etc/')
        sudo('useradd developer')
        sudo('passwd developer')
        put('/home/ndot/Desktop/itacl', '/home/ndot/')
        sudo('passwd ndot')
        exit()
     one()
def main():

    ver = raw_input("\nGoogle-chrome[1] \nChromium-browser[2] \nFirefox[3] \nFilezilla[4] \nSKYPE[5]  \nRobomongo[6] \nLAMP[7] \nAndroidStudio[8] \nSublime[9] \nEclipse[10] \nBDE[11] \nQuit[q]:")

    if ver == '1':
        print("Google Chrome")
        google_chrome()
        main()
    elif ver == '2':
        print("chromium")
        chromium()
        main()
    elif ver == '3':
        print('firefox')
        firefox()
        main()
    elif ver == '4':
        print("filezilla")
        filezilla()
        main()
    elif ver == '5':
        print("skype")
        skype()
        main()
    elif ver == '6':
        print("robo3t")
        robo()
        main()
    elif ver == '7':
        print("LAMP")
        lamp()
        main()
    elif ver == '8':
        print("android-studio")
        andr()
        main()
    elif ver == '9':
        print("sublime")
        sublime()
        main()
    elif ver == '10':
        print("eclipse")
        ecli()
        main()    
    elif ver == '11':
        print("BDE")
        google_chrome()
        chromium()
        firefox()
        skype()
        two()
	main()
    else:
        print("Sorry! \nThank you")
main()
  
