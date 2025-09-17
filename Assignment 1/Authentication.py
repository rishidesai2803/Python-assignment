real_user = "admin" 
real_pass = "1234"

user = input("Enter username: ") 
pwd = input("Enter password: ")

if user == real_user and pwd == real_pass:
    print("Login successful") 
else:
    print("Login failed") 
