import re

string1 = 'Temperature today is 72.5 degrees.'
string2 = 'I am happy today.'
string3 = 'I bought 5.2lb of apples and 2.4lb of pears.'

result = re.search(r'\d+\.\d+', string1)
if (result != None):
    print(result.group(0) + ' was found at index ' + str(result.start() + ' and ends at index ' + str(result.end())))
else:
    print('No float number found!')


