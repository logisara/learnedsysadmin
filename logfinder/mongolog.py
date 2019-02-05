from fabric.api import *
env.user = 'centos'
file=raw_input("Pem name:")
env.key_filename = '/home/ndot/'+file+'.pem'
def doc():
    print("Note:For Todays date no need .gz")
    pack=raw_input("In which name need to save:")
    choice = ' ' 
    while choice != 'q':
        choice = raw_input("\nHow many days:")

        if choice == '1' :
            date=raw_input("date[yearmonthdate.gz]:")
            run('sudo zip -r /var/www/'+livename+'/'+pack+'.zip /var/log/mongodb/mongod.log-'+date)
        elif choice == '2' :
            date=raw_input("date[yearmonthdate.gz]:")
            date1=raw_input("date1[yearmonthdate.gz]:")
            run('sudo zip -r /var/www'+livename+'/'+pack+'.zip /var/log/mongodb/mongod.log-'+date+' /var/log/mongodb/mongod.log-'+date1)
        elif choice == '3' :
    	   date=raw_input("date[yearmonthdate.gz]:")
           date1=raw_input("date1[yearmonthdate.gz]:")
           date2=raw_input("date2[yearmonthdate.gz]:")
           run('sudo zip -r /var/www/'+livename+'/'+pack+'.zip /var/log/mongodb/mongod.log-'+date+' /var/log/mongodb/mongod.log-'+date1+' /var/log/mongodb/mongod.log-'+date2)
        elif choice == 'q' :
           print("\nSee you later.\n")
        else:
           print("\nOnly 3 days\n")

livef=raw_input("Enter the Live File Name:")
sudo("grep -n "+livef+" /etc/httpd/conf/httpd.conf")
#livefname=raw_input("Enter the Root Document file[html or vhosts/filename]:")
livename=raw_input("Enter the Root Document file[html or vhosts/filename]:")
doc()
