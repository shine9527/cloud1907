import paramiko


def exec_remote_machine_command(ip, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=user, password=passwd)
    def exec(command):
        stdin, stdout, stderr = ssh.exec_command(command=command, timeout=1)
        print(stdout.read().decode('utf-8'))
        ssh.close()
    return exec


client = exec_remote_machine_command('1.1.1.1', 'root', 'xxxx')
client('ls -l /opt')

