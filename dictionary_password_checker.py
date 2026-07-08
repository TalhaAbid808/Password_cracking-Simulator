password = input("Enter password: ")
found = False
with open("passwords.txt","r") as file:
    for line in file:
        # print(line.strip())
        
     if password ==line.strip:
        found=True
        break
if found:
    print("weak password")
else:
    print("password not found in common password list")