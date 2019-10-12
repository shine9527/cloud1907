# 请使用paramiko来建立一个可以在远程机器中上传和下载的工具
import paramiko


def gpfile(style, ip, port=22, user='root', idrsa_path='/root/.ssh/id_rsa'):
    trans = paramiko.Transport((ip, port))
    trans.connect(username=user, pkey=paramiko.RSAKey.from_private_key_file(idrsa_path))
    sftp = paramiko.SFTPClient.from_transport(trans)
    def putfile(local, remote):
        sftp.put(localpath=local, remotepath=remote)
    def getfile(remote, local):
        sftp.get(remotepath=remote, localpath=local)
    if style in ('download', 'get'):
        return getfile
    else:
        return putfile


put = gpfile(style='put', ip='39.100.110.135', idrsa_path='/Users/liuchao/.ssh/id_rsa')
put(local='create_terminal.py', remote='/opt/terminal.py')


