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
def htm():
    pack=raw_input("In which name need to save:")
    month=raw_input("month:")
    livef=raw_input("Enter the Live File Name:")
    sudo("grep -n "+livef+" /etc/httpd/conf/httpd.conf")
    livename=raw_input("Enter the Root Document file[html or vhosts/filename]:")
    choice = ' ' 
    with cd('/var/www/'+livename+'/application/logs/2017/'+month+'/'):
        while choice != 'q':
            choice = raw_input("\nHow Many Days:")

            if choice == '1' :
                date=raw_input("date:")
                run('sudo zip -r /var/www/'+livename+'/'+pack+'.zip '+date+'.php')
            elif choice == '2' :
                date=raw_input("date:")
                date1=raw_input("date1:")
                run('sudo zip -r /var/www/'+livename+'/'+pack+'.zip '+date+'.php '+date1+'.php')
            elif choice == '3' :
                date=raw_input("date:")
                date1=raw_input("date1:")
                date2=raw_input("date2:")
                run('sudo zip -r/var/www/'+livename+'/'+pack+'.zip '+date+'.php '+date1+'.php '+date2+'.php')
            elif choice == 'q' :
                print("\nSee you later.\n")
            else:
                print("\nOnly 3 days\n")

    

def mon():
    print("Note:For Todays date no need .gz")
    pack=raw_input("In which name need to save:")
    livef=raw_input("Enter the Live File Name:")
    sudo("grep -n "+livef+" /etc/httpd/conf/httpd.conf")
    livename=raw_input("Enter the Root Document file[html or vhosts/filename]:")
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

    

#main program
morh=raw_input("Mongolog[1] weblog[2]:\n")
if morh == '2':
    htm()
elif morh == '1':
    mon()
else :
    Print("Sorry")