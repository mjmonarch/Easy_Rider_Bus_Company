import re

string = input()

result =re.findall(r'(?<=\$)\d+', string)
result = map(lambda x: int(x), result)

print(f"This week you have spent: {sum(result)} dollars")
