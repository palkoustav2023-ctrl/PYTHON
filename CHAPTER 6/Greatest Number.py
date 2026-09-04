#Program to find the greatest of four numbers entered by the user.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
d = int(input('Enter the fourth number: '))

if b<a and c<a and d<a:
    print(a, 'is the greatest.')
elif a<b and c<b and d<b:
    print(b, 'is the greatest.')
elif a<c and b<c and d<c:
    print(c, 'is the greatest')
else:
    print(d, 'is the greatest.')