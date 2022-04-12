import re

string = input()

string = re.sub("^@\w+", "<AUTHOR>", string)
string = re.sub("@\w+", "<HANDLE>", string)

print(string)