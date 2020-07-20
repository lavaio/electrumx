#!/usr/bin/python
import time
import subprocess

def cmd(command):
    #subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(command)
    ret = subprocess.check_output(command, shell=True)
    return ret   

def get_cmd_pid(cmd_str):
    ret = cmd(cmd_str)
    print(ret)
    if not ret.strip():
        return None
    str_list = ret.split()[0].split("/")
    return str_list[0]
    
def main():
    # 1. find
    cmd_str = "netstat -ntlp | grep '60999' | grep -v 'grep' | awk '{print $7}'"
    pid = get_cmd_pid(cmd_str)
    print(pid)
    # 2. kill
    if pid:
        cmd_str = "kill -2 " + pid
        cmd(cmd_str)
    # 3. start
#        cmd_str = ". ./run.sh && nohup ./electrumx_server &"  
#        cmd(cmd_str)

if __name__ == "__main__":

#    while True:
       try:
           main()
       #print(message_infos_rates(db, '2019-09-30T02:32:30Z'))
       except Exception as ex:
           print ('error : ', ex)
#       time.sleep(20)

