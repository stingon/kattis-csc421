Created on Tue Nov 10 17:34:56 2020

@author: dt
"""

number = int(input())
possibleResults={}
ops=['+','-','*','//']

for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            equationStr= ' 4 ' + op1 + ' 4 '+ op2 + ' 4 '+op3+' 4 '
            result=eval(equationStr)
            possibleResults[result]=equationStr.replace('//','/')
            
for i in range(number):
    n = int(input())
    if n>256:
        print('no solution')
    elif n in possibleResults.keys():
        print(possibleResults[n] + '= '+str(n))
    else:
        print('no solution')
