# print("Hello world")
# reverse=0
# number=int(input("Enter Your Number: "))
# while number!=0:
#     num=number%10
#     reverse=reverse*10+num
#     number//=10
# print(reverse)

# while True:
#     num=int(input("Enter a number: "))
#     if num>0:
#         print("it is postive")
#     elif num <0:
#         print("it is nagetive")
#     else:
#         print("it is zero")


# units=int(input("Enter: "))
# if units > 0 and units <=100:
#     bill=units*10
# elif units >=100 and units <=200:
#     bill=100*10+(units-100)*15
# else:
#     bill=100*10+100*15+(units-100)*15

# print("Bill: ",bill)



num=int(input("Enter: "))
for i in range(1,num):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)