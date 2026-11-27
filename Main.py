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



# num=int(input("Enter: "))
# for i in range(1,num):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# sum=0
# n=int(input("Enter Number: "))
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# count=0
# n=int(input("Enter Number: "))
# while n>0:
#     n//=10
#     count+=1
    
# print(count)

# a=input("Enter string: ")
# b=''
# for char in a:
#     b=char+b

# if a==b:
#     print("Yes")
# else:
#     print("No")


# n=int(input("Enter Number: "))
# table=int(input("Enter Table: "))

# for i in range(1,n+1):
#     print(f"{i} x {table} = {i*table}")



# even_sum=0
# odd_sum=0
# number=int(input("Ener number: "))
# for i in range(1,number+1):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i

# print("Even Sum: ",even_sum)
# print("Odd Sum: ",odd_sum)

# number=int(input("Enter Number: "))
# if number<=1:
#     print("Not Prime")
# else:
#     for i in range(2,number):
#         if number%i==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")


# number=int(input("Enter Number: "))
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=int(input("Enter Number: "))
# for i in range(1,n+1):
#     if n==0 or n==1:
#         print()

# fact=1
# n=int(input("Enter Number: "))
# for i in range(1,n+1):
#     if n<0:
#         print("Factorial is not Defined")
#     else:
#         fact*=i

# print("The Factorial is: ",fact)

# num1=int(input("Enter Number 1: "))
# num2=int(input("Enter Number 2: "))
# n=int(input("Enter Number: "))
# max_div=0
# for i in range(1,n+1):
#     if(num1%i==0 and num2%i==0):
#         max_div=i

# print("The max div is: ",max_div)

# list1=[1,2,3,4,5,6,6,7,4]
# list2=[]

# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def division(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b


# while True:
#     print("\n1 - Add")
#     print("2 - Sub")
#     print("3 - Mul")
#     print("4 - Div")
#     print("5 - Exit")

#     n = input("Enter what to do: ")

#     if n in ['1', '2', '3', '4']:
#         a = int(input("Enter Number 1: "))
#         b = int(input("Enter Number 2: "))

#         if n == '1':
#             print("Result:", add(a, b))

#         elif n == '2':
#             print("Result:", sub(a, b))

#         elif n == '3':
#             print("Result:", mul(a, b))

#         elif n == '4':
#             print("Result:", division(a, b))

#     elif n == '5':
#         print("Calculator Closed")
#         break

#     else:
#         print("Invalid Choice")

# numbers=[12,34,55,44]
# largest=float("-inf")
# Second=float("-inf")

# numbers = [12, 34, 55, 44]

# largest = float("-inf")
# second = float("-inf")

# for num in numbers:

#     if num > largest:
#         second = largest
#         largest = num

#     elif num > second and num < largest:
#         second = num

# if second == float("-inf"):
#     print("There is no second largest")
# else:
#     print("Second Largest:", second)