# Program to get a number and check whether that number is divisible by 3 or 5
# and prints the numbers from 1 to that number

# solution 
number = input("please enter a number: ")
n=1 
while n <= int(number):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("fuzz")
    else:
        print(n)
    n = n + 1

#a better solution
number = int(input("please enter a number: "))

for i in range(number):
	if i % 3 ==0 and i % 5 == 0:
		print("fizzbuzz")
	elif i % 5 == 0:
		print("buzz")
	elif i % 3 == 0:
		print("fizz")
	else:
		print(i)
