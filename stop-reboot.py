import time
import subprocess
import datetime

def Com_ack():
    loss_pat='0 packets received'
    msg_pat='icmp_seq=1'
    management_ip = "127.0.0.1"
    ping = subprocess.Popen(
        ["ping","-c","1", "-i", "5", management_ip],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    message = ''

    for line in out.splitlines():
        if line.find(msg_pat)>-1:
            message = line.split(msg_pat)[1]
        if line.find(msg_pat)>-1:
            flag=False
            break
    else:
        flag = True
    if flag:
        print '[ OK ] ' + 'Connection success to ' + management_ip + ' at ' + datetime.datetime.now().strftime('%x %X')
    else:
        print '[ NO ]' + datetime.datetime.now().strftime('%x %X')
        subprocess.call(["service", "cloudstack-agent", "stop"])
        
if __name__ == '__main__':
    while True:
        Com_ack()
        time.sleep(75)
