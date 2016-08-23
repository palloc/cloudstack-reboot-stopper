import time
import subprocess
import datetime
import sys

def Com_ack():
    loss_pat='0 packets received'
    management_ip = "127.0.0.1"
    counter = 0
    with open('cloudstack_access.log', 'w') as log_file:
        for i in range(3):
            # send ping
            ping = subprocess.Popen(
                ["ping","-c","1", "-i", "15", management_ip],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, error = ping.communicate()
        
            for line in out.splitlines():
                if loss_pat in line:
                    flag = False
                else:
                    flag = True
            if flag:
                log_file.write('[ OK ] ' + 'Successed to connect ' + management_ip + ' at ' + datetime.datetime.now().strftime('%x %X') + '\n')
            else:
                log_file.write('[ NO ]' + 'Failed to connect ' + datetime.datetime.now().strftime('%x %X') + '\n')
                counter += 1
        
            # failed connect
            if counter == 3:
                agent_stop = subprocess.Popen(
                    ["service", "cloudstack-agent", "stop"],
                    agent_stdout = subprocess.PIPE,
                    agnet_stderr = subprocess.PIPE
                )
                out, error = agentstop.communicate()
                manage_stop = subprocess.Popen(
                    ["service", "cloudstack-management", "stop"],
                    manage_stdout = subprocess.PIPE,
                    manage_stderr = subprocess.PIPE
                )
                out, error = agentstop.communicate()            
                log_file.close()
                sys.exit()


if __name__ == '__main__':
    while True:
        Com_ack()
        time.sleep(75)
        
