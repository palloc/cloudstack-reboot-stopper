import time
import subprocess
import datetime

def Com_ack():
    loss_pat='0 packets received'
    management_ip = "127.0.0.1"
    counter = 0
    for i in range(3):
        ping = subprocess.Popen(
            ["ping","-c","1", "-i", "15", management_ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        message = ''
        
        for line in out.splitlines():
            if loss_pat in line:
                message = line.split(msg_pat)[1]
                flag = False
            else:
                flag = True
            if flag:
                print '[ OK ] ' + 'Successed to connect ' + management_ip + ' at ' + datetime.datetime.now().strftime('%x %X')
            else:
                print '[ NO ]' + 'Failed to connect 'datetime.datetime.now().strftime('%x %X')
                counter += 1
                break
        if counter == 3:
            agentstop = subprocess.Popen(
                ["service", "cloudstack-agent", "stop"],
                agentstdout = subprocess.PIPE,
                agnetstderr = subprocess.PIPE
            )
            out, error = agentstop.communicate()
            managementstop = subprocess.Popen(
                ["service", "cloudstack-management", "stop"],
                managestdout = subprocess.PIPE,
                managestderr = subprocess.PIPE
            )
            out, error = agentstop.communicate()            



if __name__ == '__main__':

    while True:
        Com_ack()
        time.sleep(75)
        
