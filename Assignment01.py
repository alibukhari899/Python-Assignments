#Question no 1
print("Twinkle Twinkle Little star\n \t How I Wonder What You Are\n \t \t Up Above The World So High \n \t \t Like a Diamond In The Sky\n Twinkle Twinkle Little Star\n \t How I wonder What You Are ")

#Question No 2
import platform
print(platform.python_version())

#Question N0 3
import time 
print(time.ctime())

#Question No 4
Radius=float(input("enter radius "))
check=int(Radius)
if Radius<=0 :
    print("area does not exist")
elif Radius==check :
    print("the area of circle with radius " + str(check) + " is " + str(Radius*Radius*2*3.142))  
else:
    print("the area of circle with raidus " + str(Radius) + " is " + str(Radius*Radius*2*3.142))

#Question No 5
first_name=str(input("Entre your first name:\t"))
last_name=str(input("Entre your last name:\t"))
print(last_name+" "+first_name)

#Question No 6
value_01=int(input("Entre First number:\t"))
value_02=int(input("Entre Second Number:\t"))
result=str(value_01+value_02)
print("The addition of given two numbers is:\t"+""+result)
