import hashlib
#Sign-Up
email=input("Enter you email")
password=input("Enter your password")
confirm_password=input("Confirm your password")
if confirm_password==password:
    e=confirm_password.encode()
    h1=hashlib.md5(e).hexdigest()
    with open("userinfo.txt","w") as f:
        f.write(email+"\n")
        f.write(h1)
        f.close()
        print("You have signed up successfully")
else:
    print("Password is not same as above! \n")
