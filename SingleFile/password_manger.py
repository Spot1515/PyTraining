from cryptography.fernet import Fernet

#import cryptography




def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
#write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            #print(line.rstrip())
            print(f"Account: {user} | Password: {fer.decrypt(passw.encode()).decode()}")





#master_pwd = input("What is the master password")

key = load_key() #+ master_pwd.encode()

fer = Fernet(key)

mode = input("What mode add passord or view password. (add, view)").lower()


if mode == "add":
    print("Add Mode")
    add()
elif mode == "view":
    print("View Mode")
    view()
else:
    print("Invalid entry:")