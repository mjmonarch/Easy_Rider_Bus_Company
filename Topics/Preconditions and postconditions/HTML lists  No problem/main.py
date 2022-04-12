import re

string = input()

result = re.findall(r'(?<=<li>).*?(?=</li>)', string)
print(*result, sep='\n')


