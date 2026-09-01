#Program to create a dictionary of Hindi words with values as their English translation.
dict = {
    'Banana':'কলা',
    'Grapes':'আঙুর',
    'Apple':'আপেল',
    'Pineapple':'আনারস',
}

user = input('Enter the word you want to translate: ')
if user in dict:
    print(dict[user], 'is the translation')