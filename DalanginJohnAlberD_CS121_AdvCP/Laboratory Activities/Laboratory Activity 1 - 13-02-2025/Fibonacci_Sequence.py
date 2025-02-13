term = int(input("Enter the number of terms: "))
num_count = 0
first = 0
second = 1
print("Fibonacci Series:", end = " ")
while num_count < term:
    print(first, end = ' ')
    result = first + second 
    first = second
    second = result
    num_count += 1
