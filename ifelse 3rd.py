preusername = "admin"
prepassword = 1234

username = input("enter username :")
password = int(input("entre password :"))

if username == preusername:
    if password == prepassword:
        print("login sucessfull")
    else:
            print("invalid password")
else:
    print("invalid username")
