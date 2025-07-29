
while True: 
    user_numb= input("Enter a number:")
    if user_numb.isnumeric():
        numb= int(user_numb)
        break
    else:
        print("I SAID NUMBER, YOU IDIOT")
x= (numb*(numb+1))//2
print(x)
