import paramiko


# ssh-keygen -m PEM -t rsa
# private = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')
# transport = paramiko.Transport(('39.100.110.135', 22))
# transport.connect(username='root', pkey=private)
# ssh = paramiko.SSHClient()
# ssh._transport = transport
#
# stdin, stdout, stderr = ssh.exec_command(command='ls -l /etc', timeout=1)
# print(stdout.read().decode('utf-8'))
#
# transport.close()


private = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')
transport = paramiko.Transport(('39.100.110.135', 22))
transport.connect(username='root', pkey=private)

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put(localpath='kingdoms.txt', remotepath='/opt/kingdoms.txt')
sftp.get(remotepath='/root/file_opera/file.txt', localpath='./file001.txt')

transport.close()



