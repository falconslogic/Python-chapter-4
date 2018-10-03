##Textbook Chapter 3 Programming Exercise 14, PP 81
##By Blake Baker

def main():
    n = eval(input("Please enter the amuount of numbers you want to sum: "))
    sum = 0
    for i in range(n):
        sum += eval(input("Enter each number one at a time: "))
    print (float(sum/n))
    ##It originally printed a float without me changing it

main()
