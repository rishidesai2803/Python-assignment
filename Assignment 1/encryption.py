import hashlib 
user = input("Enter username: ") 
pwd = input("Enter password: ") 
# stored values 
saved_user = "better_call_saul" 
saved_pwd = hashlib.sha256("1234".encode()).hexdigest() 
# check 
if user == saved_user and hashlib.sha256(pwd.encode()).hexdigest() == saved_pwd:
    print("Login successful") 
else:
    print("Login failed")
