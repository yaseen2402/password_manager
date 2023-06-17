from cryptography.fernet import Fernet
import time

def key_loader():
    f = open("key.key","rb")
    key = f.read()
    f.close()
    return key

key =key_loader()
fer = Fernet(key)

def add():
    uname = input("enter username : ")
    upass = input("enter password : ")

    with open("pass_file.txt","a") as f:
        f.write(uname +" | "+fer.encrypt(upass.encode()).decode()+"\n")
    print("")    

def access():
    with open ("pass_file.txt","r") as f:
        for i in f.readlines():
            details = i
            usern , passwd = details.split('|')   
            print("User:",usern, "|","Password:",fer.decrypt(passwd.encode()).decode()) 



# master_key = input("enter master_key : ").strip()

time.sleep(0.2)


while True :
    option = input("ENTER '1' TO ADD NEW PASSWORD\nENTER '2' TO ACCESS EXISTING PASSWORDS\nENTER '3' TO QUIT\n")
    
    if option == '1':
        add()

    elif option == '2':
        access()

    elif option == '3':
        break

''''def key_gen():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''