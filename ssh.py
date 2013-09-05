
import paramiko


def getSSHconnection(host,uid,pwd,keyfile):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #In case the server's key is unknown, we will be adding it automatically to the list of known hosts
    ssh.connect(host, username=uid, password=pwd, key_filename=keyfile)
    return ssh

def curlGetFromSSH(ssh, request):
    stdin, stdout, stderr = ssh.exec_command(request)
    return stdout.readlines()

def closeSSH(ssh):
    ssh.close()





__author__ = 'zach.bolian'
