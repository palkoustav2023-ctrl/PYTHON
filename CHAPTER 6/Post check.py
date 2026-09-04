#Program to find out whether a given post is talking about "Harry" or not.
post = input('Enter the post: ')

if 'Harry'.lower() in post.lower():
    print('This post is stalking about Harry')
else:
    print('This post is not stalking about Harry.')