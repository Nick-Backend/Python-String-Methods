username = input(" Enter Username: ")
resault = username.replace("-","")

if resault.isalnum():
    print(True)

else:
    print(False)


