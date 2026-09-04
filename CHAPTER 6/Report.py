'''Program to find out whether a student has passed
or failed if it requires a total of 40% and at least 33% in each subject to pass.'''

english = int(input('Enter your marks in English: '))
math = int(input('Enter your marks in Mathematics: '))
science = int(input('Enter your marks in Science: '))
total = ((english + math + science)/3)

if total>=40 and english>=33 and math>=33 and science>=33:
    print('You have passed.')
else:
    print('You have failed.')