import hashlib

user = input("Enter username: ") 
pwd = input("Enter password: ")

saved_user = "John snow" 
saved_pwd_hash = hashlib.md5("1234".encode()).hexdigest() 
entered_pwd_hash = hashlib.md5(pwd.encode()).hexdigest()

if user == saved_user and entered_pwd_hash == saved_pwd_hash:
    print("Login successful") 
else:
    print("Login failed") 
