num =int(input("Enter a number: "))
number_sum = 0
for i in range(1,num):
    if(num % i == 0):
        number_sum = number_sum + i
if(number_sum == num):
    print(f"{num} is a perfect number")
else:
     print(f"{num} is not a perfect number")    
