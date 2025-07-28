list = [] # Initialize an empty list.
numb= input() 
numb= 5
i=0 # Initialize i to 0.
while i <=numb: # Run the loop as long as i is less than or equal to numb.
    list.append(i)  # Append the current value of i to the list.
    res= sum(list)  #Calculate the sum of the list.
    i+=1 # Increment i by 1.
print(res) #Print the final sum.

#Gauss's formula
numb1= 5
x= (numb1*(numb1+1))//2
print(x)

sum = 0 #Initializes a variable sum to 0, which will be used to accumulate the sum.
for i in range(numb1+1): #creates a loop that will iterate over the numbers from 0 to num1.Since num1 = 5, the loop will iterate over the numbers 0, 1, 2, 3, 4, 5
    sum += i #On each iteration, the value of i will be added to the variable sum

print(sum)