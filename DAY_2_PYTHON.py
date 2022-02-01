str='hello coders'
print('Choose any one alphabet from the word',str,'to win the lottery')
s=input('').lower()
if s==str[0] or s==str[1] or s==str[4] or s==str[6] or s==str[8]:
    print('Congratulations :) You Win the Lottery')
else:
    print('You loose :(\nBetter luck next time')
    
