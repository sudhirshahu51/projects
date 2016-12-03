cp = float(input('Enter the cost price'))
sp = float(input('Enter the selling price'))
if cp > sp:
    print('seller has made a loss of %0.2f' % (cp - sp))
elif cp < sp:
    print('seller has made a profit of %0.2f' % (sp - cp))
else:
    print('there was no profit no loss')
