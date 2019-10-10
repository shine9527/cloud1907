import paramiko

# rsa_key: command: ssh-keygen -m PEM -t rsa
private = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('39.100.110.135', 22, 'root', pkey=private)

stdin, stdout, stderr = ssh.exec_command('ls -l /etc', timeout=1)
print(stdout.read().decode('utf-8'))

ssh.close()