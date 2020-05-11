# this code gets a number from user and then prints the the word "wow" with
# the number of times the letter o that the user defined at the first


#solution
number = input("please enter a number: ")
times = int(number)
middleO= "o"
print("w"+times*middleO+"w")

#a better solution
num = int(input("please enter a number: "))
print(f"w{'o'*numb}w")

