#Program to print a letter template with name and date entered by user.
name = input("Enter your name: ")
date = input("Enter today's Date: ")
letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))