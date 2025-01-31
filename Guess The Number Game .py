import random
import time
from random import randrange as rg
num = rg(1,101)
trying = 0
level = int(input("(1) hard or  (2)normal or (3) easy : "))
if level == 1 :
    trying = 5
elif level == 3 :
    trying = 11 
else :
    trying =8 
while trying > 0: 
    s_time = time.time()
    numin = int(input(" guess a number in range (0 to 100) : "))
    thetime = time.time() - s_time
    if  thetime > 10:
        print("  Time out ")
        break
    trying -=1 
    if trying == 0:
        print ("Game Over , the number is : ",num)
    elif 0 > num or num >100:
        print("Enter a number in range (0 to 100 )", " , you have ",trying ,"Attempts")
        continue
    elif num > numin :
        print("Enter A greater than : ",numin, " , you have ",trying ,"Attempts")
        continue
    elif num < numin :
        print("Enter a less than : ",numin, " , you have ",trying ,"Attempts")
        continue
    elif num == numin :
        print ("Correct ! , The Number Is : ",num)
        break
