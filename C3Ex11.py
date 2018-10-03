##Exercise 11 pg 81
##Blake Baker
##
##Obtains the sum of the first ___ numbers

def main():
    n = eval(input("Please enter natural number to proceed to"))
    sum = 0
    for i in range(1,n+1):
        sum += i
    print (sum)

main()
