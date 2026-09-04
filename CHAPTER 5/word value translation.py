#Program to create a dictionary of Hindi words with values as their English translation.
dict = {
    'Banana':'Kela',
    'Grapes':'Angoor',
    'Chair':'Kursi',
}

user = input('Enter the word you want to translate: ')
if user in dict:
    print(dict[user], 'is the translation')
