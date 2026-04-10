#1. Print numbers 1 to 10
for i in range(1,11):
  print(i)

# #2.Print even numbers (1-20)
# print("The list of even number is:")
# for n in range(1,20):
#     if n%2==0:
#         print(n)

# #3.Print odd numbers(1-20)
# print("The list of odd numbers:-")
# for n in range(1,20):
#     if n%2!=0:
#         print(n)

# #4.Sum of first 10 numbers:
# print("The sum of first 10 number is:-")
# sum=0
# for n in range(1,11):
#     sum=sum+n
# print(sum)

# #5.Multiplication Table
# n=int(input("Enter the number:-"))
# for i in range(1,11):
#     result=n * i
#     print(result)

# #6. Reverse counting(10,1)
# for i in range(10,1,-1):
#     print(i)

# #7.Count digits in number
# n=int(input("Enter the number:-"))
# # count=0
# # while n>0:
# #     n=n//10
# #     count=count+1
# # print(count)

# #8.Sum of digits
# n=int(input("Enter the number:-"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

# #9.Factorial number:-
# n=int(input("Enter the number:-"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)

# #10. Print characters of string
# n=str(input("Enter any string:- "))
# for ch in n:
#     print(ch)

# #11.Count vowels
# n=str(input("Enter the string:-"))
# count=0
# for ch in n:
#     if ch.lower() in 'aeiou':
#         count=count+1
#         print(count)

# #12.Find largest number
# numbers=[3,7,2,9,5]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest) 

# #13. Print square numbers
# print("Here is the square of the number between 1-10:-")
# for i in range(1,11):
#     print(i*i)

# #14.Print Cube numbers
# print("Here is the cube of numbers between 1-10:-")
# for i in range(1,11):
#     print(i**3)

# #15.Sum of even numbers
# n=int
# sum=0
# for n in range(1,50):
#     if n%2==0:
#         sum=sum+n
# print("The sum of all even number is:-",sum)

# 16. Reverse a number
n=123
temp=n
rev=0
while temp>0:
 rem=temp%10
 temp//=10
 rev=rev*10+rem
print("Reversed number:-",rev)

# #17.Palindrome number
# n=int(input("Enter the value for checking the given number is palindrome or not:-"))
# temp=n
# rev=0
# while temp>0:
#     rem=temp%10
#     temp//=10
#     rev=rev*10+rem
# if rev==n:
#     print("This number is Palindrome number:-",rev)
# else:
#     print("This number is not palindrome number:-",n)
