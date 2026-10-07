# a = "Hello how are you"
# print(a[6:10])
# print(a[-3:])
# print(a[0:5])

# Accept two numbers and print the greatest between them.

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number: "))
# if a>b:
#     print(f"{a} is greater number")
# elif a==b:
#     print(f"{a} and {b} are equal number")
# else:
#     print(f"{b} is greater number")

# Accept gender from user and print a greeting message.

# gender = input("Enter your gender in M or F :")
# if gender == "M" or gender == "m": 
#     print("Good morning sir")
# elif gender == "F" or gender == "f":
#     print("Good morning Mam")
# else:
#     print("others")

# Accept an integer and check if it is even or odd.

# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# Accept a year and check if it is a leap year.

# year = int(input("Enter a number : "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Accept temperature in °C and print a description.

# Input: -5
# Freezing Cold 
# Input: 25
# Pleasant 
# Input: 45
# Very Hot 

# temp = int(input("Enter temperature in °C : "))
# if (temp<5): {
#     print("Freezing Cold 🥶
# }
# elif (temp<35): {
#     print("Pleasant )
# }
# else:
#     print("Very Hot")

# 5 ka table by Loop

# for i in range(1,11,1):
#     print("5","x",i,"=",5*i)

# Print "Hello World" n times.

# a = int(input("Enter a number: "))
# for i in range(1,(a+1)):
#     print("Hello World")

# Print natural numbers from 1 to n.

# num2 = int(input("Enter a number: "))
# for i in range(1,(num2+1)):
#     print(i)

# Reverse for loop — print n down to 1.

# num3 = int(input("Enter a number: "))
# for i in range(num3,0,-1):
#     print(i)

# Sum of first n natural numbers.

# num4 = int(input("Enter a number: "))
# sum = 0
# for i in range(num4,0,-1):
#     sum+=i
# print(sum)

# Factorial of a number.

# num5 = int(input("Enter a number: "))
# factorial= 1
# for i in range(num5,0,-1):
#     factorial*=i
# print(factorial)

# Print sum of all even and odd numbers in a range separately.

# num6 = int(input("Enter a number: "))
# evenSum = 0
# oddSum = 0 
# for i in range(1,(num6+1)):
#     if i % 2 == 0: 
#         evenSum+= i
#     else:
#         oddSum+=i
# print(f"Sum of Even no. is {evenSum}")
# print(f"Sum of odd no. is {oddSum}")

# Print all factors of a number.

# num7 = int(input("Enter a number: "))
# for i in range(1,(num7+1)):
#     if num7 % i == 0:
#         print(i)

# Check if a number is perfect (sum of factors = the number itself).

# num8 = int(input("Enter a number: "))
# sum = 0
# for i in range(1,(num8)):
#     if num8 % i == 0:
#         sum+=i
#         # print(sum)
# if sum == num8:
#     print(f"Yes {num8} is a perfect number")
# else:
#     print(f"{num8} is not a perfect number")

# Reverse a string without using built-in functions.

# str1 = input("Enter any word: ")
# rev = ""
# for i in range((len(str1)-1),-1,-1):
#     # print(i)
#     rev =  rev + str1[i] 
# print(rev)

# Check if a string is a palindrome

# Check if a number is prime.

# num9 = int(input("Enter a number: "))
# sum = 0
# for i in range(1,num9+1):
#     if num9 % i == 0:
#         sum+=1
# if sum == 2:
#     print(f"{num9} is a prime number")
# else:
#     print(f"{num9} is not a prime number")

# Check if a string is a palindrome

# str10 = input("Enter any word: ")
# rev = ""
# for i in range((len(str10)-1),-1,-1):
#     rev =  rev + str10[i] 
# if str10 == rev:
#     print("  Palindrome ✅")
# else:
#     print("not a Palindrome") 

# Separate each digit of a number and print on a new line.

# numa = int(input("Enetr a number: "))
# while numa > 0 :
#     print(numa % 10)
#     numa = numa // 10

# Accept a number and print its reverse.

# numb = int(input("Enetr a number: "))
# rev = 0
# while numb > 0 :
#     rev = rev * 10 + numb % 10
#     numb = numb // 10
# print(rev)

# Check if a number is palindromic (equal to its reverse).

# numc = int(input("Enetr a number: "))
# num12 = numc
# rev = 0
# while numc > 0 :
#     rev = rev * 10 + numc % 10
#     numc = numc // 10
# print(rev)
# if rev == num12:
#     print("Palindrome ✅")
# else:
#     print("Not Palindrome ❌")

# Print positive and negative elements of an List

# l = [33,54,87,-76,-87,45,-655,453,-546,-65,-654,456,5,64,3,5,56,66,]
# l.sort()
# print("positive elements are :")
# for i in l:
#     if i >= 0:
#         print(i)  # positive number
# print("negative elements are :")
# for i in l:
#     if i <= 0:
#         print(i) # negative number

# Mean of List elements

# m = [33,64,56,45,45,44,6,46,4,65,64,64,4,64,564]
# sum = 0

# for i in m:
#     sum+=i
# print(f"mean of elements are : {sum/(len(m))}")

# Find the greatest element and print its index too

# n = [43,56,-766,-6,5,-76,-54,43,56,45,465,6554,54,6,5,34,334,645,4656,5656,6,767,566,564,56]
# n.sort()
# print(n[len(n)-1])


# n = [43,56,-766,-6,5,-76,-54,43,56,45,465,6554,54,6,5,34,334,645,4656,5656,6,767,566,564,56]
# num = n[0]
# indx = 0

# for i in range(0,len(n)):
#     if n[i] > num:
#         num = n[i]
#         indx = i
        
# print(num)
# print(indx)


# Find the second greatest element

# o = [68,643,6,1342,16,133479,13349,70,19,19,1743,(4432*6)]
# num = o[0]
# num2 = o[0]



# for i in range(0,len(o)):
#     if o[i] > num:
#         num2 = num
#         num = o[i]

        
#     elif o[i]> num2 and o[i] != num :
#         num2 = o[i]
#         # indx = i
        

# print(f"{num2} is 2nd largest number")

# print(f"index = {o.index(num2)}")


# Check if List is sorted or not

# p = [32,545,65,23,56,56,76,34]
# q = []
# for i in range(len(p)):
#     q.append(p[i])
# q.sort()
# print(p)
# print(q)

# if p == q:
#     print("List is sorted")
# else:
#     print("list is not sorted")

# 2nd method
# p = [1,2,2.3,4,5,5,9,23,34,34,54]

# num = p[0]
# for i in range(1,len(p)):   
#     if num <= p[i]:
#         num = p[i]
#         continue      
#     else:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")  

# Write a Python script to merge two Python dictionaries

# A = {"a":"Apple","b":"Ball","c":"cat","d":"dog"}
# B = {"e":10,"f":100,"g":1000,"h":10000}

# for i in B:
#     print(i)
#     A[i] = B[i]
# print(A)

# Write a Python program to sum all the values in a dictionary

# C = {"e":10,"f":100,"g":1000,"h":10000}
# sum = 0
# for i in C:
#     sum += C[i]
# print(sum)

# Count the frequency of each elements in list

listt = [34,456,454,4,4345,54,5345,54,5,4,6,5,65,656,45,4,5,65,6,5,5,6,5,6,6,75,6,5676,7]
d = {}

for i in listt:
    if i in d.keys():
        d[i] += 1
        # print(d)
    else:
        d[i] = 1
        # print(d) 
print(d)

# Write a Python program to combine two dictionary by adding values for common keys

# D = {1:10,2:20,3:30,4:40}
# E = {4:59,5:90,3:50,9:49}

# for i in E:
#     if i in D.keys():
#         D[i] += E[i]
#     else:
#         D[i] = E[i]
# print(D)








