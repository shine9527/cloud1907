# 请使用paramiko来建立一个可以远程执行命令的工具
import paramiko


def terminal(ip, port=22, user='root', idrsa_path='/root/.ssh/id_rsa'):
    trans = paramiko.Transport((ip, port))
    trans.connect(username=user, pkey=paramiko.RSAKey.from_private_key_file(idrsa_path))
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    while True:
        command = input('root@localhost ~ % ')
        if command in ('exit', 'logout'):
            trans.close()
            break
        _, stdout, stderr = ssh.exec_command(command=command, timeout=1)
        if len(stderr.read()) != 0:
            print(stderr.read().decode('utf-8'))
        else:
            print(stdout.read().decode('utf-8'))


terminal(ip='39.100.110.135', idrsa_path='/Users/liuchao/.ssh/id_rsa')


