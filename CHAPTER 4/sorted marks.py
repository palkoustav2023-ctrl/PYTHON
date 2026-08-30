#Program to accept marks of 6 students and display them in a sorted manner.
marks = []

m1 = int(input('Enter the marks of first student: '))
marks.append(m1)
m2 = int(input('Enter the marks of second student: '))
marks.append(m2)
m3 = int(input('Enter the marks of third student: '))
marks.append(m3)
m4 = int(input('Enter the marks of the fourth student: '))
marks.append(m4)
m5 = int(input('Enter the marks of the fifth student: '))
marks.append(m5)
m6 = int(input('Enter the marks of the fifth student: '))
marks.append(m6)

marks.sort()

print(marks)