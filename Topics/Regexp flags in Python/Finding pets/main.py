import re 

pets = input()
template = 'dog|cat|parrot|hamster'

result = re.findall(template, pets, flags=re.IGNORECASE)
print(result)
