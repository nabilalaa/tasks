""""
write a simple code to take a number from the user than check if this number is less 20 or not if it is less than 20 print the numbers from this number to 50
but increasing by 3 if it is not less than 20 print the numbers between this number and 50 but increasing by 2
"""

num = int(input("enter number: "))


if num < 20:
    for i in range(num,51,3):
        print(i)

else:
    for i in range(num+1, 50, 2):
        print(i)