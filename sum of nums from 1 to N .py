#Write a program to calculate the sum of numbers from 1 to N, where N is a number entered by the user
n =int(input("Enter Number"))
sum_nums=0
for i in range(0,n+1):
    sum_nums+=i
print("sum of numbers from 1 to ",n ," = ",sum_nums)
