import re


def tokenize(string):
    # Let's create a pattern that contains punctuation marks
    punctuation = re.compile(r'[\.,\?!\*:;()]')
    # Substitute the punctuations with empty strings
    no_punct = re.sub(punctuation, '', string)
    print(no_punct)
    # This is a sample string And here's another one
    # Split sentences by whitespaces
    tokens = re.split('\s+', no_punct)
    return tokens


string = input()
template1 = r'(?<![a-z])[A-Z]+[a-z]*'
template2 = r'\d+'

result1 = re.findall(template1, string)
result2 = re.findall(template2, string)
print(f'Capitalized words: {", ".join(result1)}')
print(f'Digits: {", ".join(result2)}')
