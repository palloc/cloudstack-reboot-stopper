import time
import subprocess
import datetime

def Com_ack():
    loss_pat='0 packets received'
    management_ip = "127.0.0.1"
    ping = subprocess.Popen(
        ["ping","-c","1", "-i", "15", management_ip],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    message = ''

    for line in out.splitlines():
        if line.find(loss_pat)>-1:
            message = line.split(msg_pat)[1]
            flag=False
            break
    else:
        flag = True
    if flag:
        print '[ OK ] ' + 'Connection success to ' + management_ip + ' at ' + datetime.datetime.now().strftime('%x %X')
        return 0
    else:
        print '[ NO ]' + datetime.datetime.now().strftime('%x %X')
    return 1

if __name__ == '__main__':
    counter = 0
    while True:
        counter += Com_ack()
        if counter > 2:
            subprocess.call(["service", "cloudstack-agent", "stop"])
            subprocess.call(["service", "cloudstack-management", "stop"])            
        time.sleep(75)
        print counter
