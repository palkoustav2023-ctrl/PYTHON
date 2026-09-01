#Program to allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.
dict = {}

n1 = input('Enter name of 1st one: ')
l1 = input('Enter your language: ')
dict.update({n1:l1})
n2 = input('Enter name of 2nd one: ')
l2 = input('Enter your language: ')
dict.update({n2:l2})
n3 = input('Enter name of 3rd one: ')
l3 = input('Enter your language: ')
dict.update({n3:l3})
n4 = input('Enter name of 4th one: ')
l4 = input('Enter your language: ')
dict.update({n4:l4})

print(dict)