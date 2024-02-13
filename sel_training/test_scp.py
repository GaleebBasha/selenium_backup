# import paramiko, scp
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.0.7', username='Lenovo', password="123", port=25)
# print(ssh)


import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.0.7', 23, 'LAPTOP-G8166CNT', '123')
scp = SCPClient(ssh.get_transport())