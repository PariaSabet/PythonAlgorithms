# this program adds the digits of an integer  repeatedly
# until the sum is a single digit

number = int(input("please enter a number"))

def sumOfDigits(x):
    summary = 0
    while x > 0:
        add = x%10
        summary = add + summary
        x = int(x/10)
    if summary > 9: 
        final = summary
        sumOfDigits(final)
    else:
        print(summary)
sumOfDigits(number)

# a better solution
i = input("")
final = sum(list(map(int,i)))
while final > 9:
	final = sum(list(map(int,str(final))))
print(final)
