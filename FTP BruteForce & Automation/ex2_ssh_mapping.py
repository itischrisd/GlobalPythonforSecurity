import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target_host = input("IP celu: ")
target_port = 22
user = input("Podaj username: ")
passwd = input("Podaj password: ")

ssh.connect(hostname=target_host, username=user, password=passwd)

stdin, stdout, stderr = ssh.exec_command('ls -l /root')

print("Dane znajdujące się w bilbiotece:\n{} \n\nBłędy:\n {} \n".format(stdout.read().decode(), stderr.read().decode()))
