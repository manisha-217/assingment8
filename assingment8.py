#Q.1 what is time tuple
import time
print(time.gmtime(0))

#Q.2 write a program to get formated time
import datetime
print(datetime.date.today())
print(time.ctime())

#Q.3 extract month from time
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)
print(l[1])

#Q.4.extract day from the time.
from datetime import datetime
now=datetime.now()
print("day:",now.strftime("%A"))

#Q.5.extract date from the time.
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)
print(l[2])

#Q.6 write a program to print time using local time method.
import time
print(time.localtime())

#Q.7 find factorial of number
import math
num=int(input("enter any number"))
print(math.factorial(num))

#Q.8 find the G.C.D of number
num1=int(input("enter first number"))
num2=int(input("enter second number"))
import math
print(math.gcd(num1,num2))

#Q.9 using os pacakage print current directory and user enviroment
import os
print(os.getcwd())
print(os.environ)
