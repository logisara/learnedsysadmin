import os;
os.system('python /home/ndot/logirocker/running/iplist/id.py -i 192:168:3:1-255 > 1.txt')
os.system('python /home/ndot/logirocker/running/iplist/id.py -i 192:168:2:1-255 > 2.txt')
os.system('python /home/ndot/logirocker/running/iplist/id.py -i 192:168:1:1-255 > 3.txt')
os.system('cat 1.txt 2.txt 3.txt > live.txt')
os.system('mail -s "Running Ips" logeshkumar@ndot.in < /home/ndot/logirocker/running/iplist/live.txt')
