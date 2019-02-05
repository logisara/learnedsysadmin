from fabric.api import *
env.user='ndot'
env.password='rAnGErs@S%s@dm!'
def teamview():
 with cd('/tmp'):
   run('wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb')
   try:
    sudo('dpkg -i teamviewer_amd64.deb')
    sudo('chmod -R 777 /usr/bin/teamviewer')
   #sudo('crontab -e')
    sudo('sed -i 16i"2 */3   * * *   root chmod -R 000 /usr/bin/teamviewer" /etc/crontab')
    sudo('service cron restart')
   except:
    sudo('dpkg -i teamviewer_amd64.deb')
    sudo('apt-get -f install')
    sudo('sed -i 16i"2 */3   * * *   root chmod -R 000 /usr/bin/teamviewer" /etc/crontab')
    sudo('service cron restart')
def anydesk():
  with cd('/tmp'):
   run('wget https://download.anydesk.com/linux/anydesk_4.0.1-1_amd64.deb')
   try:
    sudo('dpkg -i anydesk_4.0.1-1_amd64.deb')
    sudo('chmod -R 777 /usr/bin/anydesk')
   #sudo('crontab -e')
    sudo('sed -i 21i"2 */3   * * *   root chmod -R 000 /usr/bin/anydesk" /etc/crontab')
    sudo('service cron restart')
   except:
    #sudo('dpkg -i anydesk_4.0.1-1_amd64.deb')
    sudo('apt-get -f install')
    sudo('chmod -R 777 /usr/bin/anydesk')
   #sudo('crontab -e')
    sudo('sed -i 21i"2 */3   * * *   root chmod -R 000 /usr/bin/teamviewer" /etc/crontab')
    sudo('service cron restart')
def uninstallteam():
    sudo('apt-get purge teamviewer')
    #sudo('apt-get purge anydesk')
def uninstallany():
    sudo('apt-get purge anydesk')

def main():
    ver = raw_input("\nTeamviewer[1] \nAnydesk[2] \nUninstall-Teamv[3] \nUninsll-anydesk[4] \nQuit[q]:")
    if ver =='1':
        teamview()
        main()
    elif ver =='2':
        anydesk()
        main()
    elif ver =='3':
	uninstallteam()
	main()
    elif ver =='4':
	uninstallany()
	main()
    else:
	exit()
main()
