import re

string = input()
start = "<START>"
end = "<END>"

start_index = re.search(start, string).end()
end_index = re.search(end, string).start()
print(string[start_index:end_index])
