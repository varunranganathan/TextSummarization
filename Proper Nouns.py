import nltk.data
from nltk.tag import pos_tag
import re
from nltk.tokenize import word_tokenize
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
f = open("text3.txt", 'r')
g = open("ans.txt",'w')
data = f.read()
i = 1 
for p in data.split('\n\n'):   
	x = pos_tag(p.split())
	for s in tokenizer.tokenize(p.strip()):
	propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
for a in propernouns:
	g.write(propernouns[a])
				
