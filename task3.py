import random
balance= 10 #initial balance of the user

def slot_machine(balance):

    while balance>0: #loop runs as long as the user has money
        input("Press any key to start: ") #initial input
        n=3 
        user_number= random.sample(range(0,9), n) #gives 3 random numbers
        print(user_number)
# Check if the user won (all three numbers are 7)
        if user_number== [7, 7, 7]:
            print("You won a 100 euros")
            balance+=100
            print("Remaining balance", balance)
            
        else: 
            print("You lost")
            balance-=1
            print("Remaining balance", balance)
            

if balance>0:
    slot_machine(balance)

    
else:
    print("You don't have enough money to play")
    
        

