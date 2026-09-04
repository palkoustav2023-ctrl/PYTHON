#Program to detect spams.
p1 = 'Make a lot of money'.lower()
p2 = 'Buy now'.lower()
p3 = 'Subscribe this'.lower()
p4 = 'Click this'.lower()
sentence = input('Enter your sentence: ')

if p1 in sentence or p2 in sentence or p3 in sentence or p4 in sentence:
    print('This sentence is a spam!')
else:
    print('This sentence is not a spam.')