username = input("enter your username=")
password =input("enntern your pasword=")

if username =="admin" and password =="1234":
    print("login succesfull")
else:
    print("login failed")

    if username != "admin":
        print("invalid username")
    else:
        print("invlaid password")
