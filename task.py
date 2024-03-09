import nltk

# you can write any two words to be treated like a one word

skip_word=r'\b(?:Los\sAngelos)\b|\w+'

# string="Hi ,im a gamer, i live in Los Angelos"
string=str(input("Enter your text : "))
tokenizer = nltk.RegexpTokenizer(skip_word)

word=tokenizer.tokenize(string)

print(word)




