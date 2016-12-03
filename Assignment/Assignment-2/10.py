a = input('Enter the character')
a = ord(a)
if a in range(65, 91):
    print('Capital letter')
elif a in range(97, 123):
    print('small letter')
elif a in range(48, 58):
    print('decimal letter')
else:
    print('special character')
