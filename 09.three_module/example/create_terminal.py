import paramiko


trans = paramiko.Transport(('39.100.110.135', 22))
trans.connect(username='root', pkey=paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa'))
ssh = paramiko.SSHClient()
ssh._transport = trans

while True:
    command = input('root%39.100.110.135:$ ')
    stdin, stdout, stderr = ssh.exec_command(command=command, timeout=1)
    if command in ('exit', 'logout'):
        trans.close()
        break
    elif len(stderr.read()) > 0:
        print(stderr)
    else:
        print(stdout.read().decode('utf-8'))
