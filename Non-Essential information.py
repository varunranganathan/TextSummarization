import nltk.data
import re
from nltk.tokenize import word_tokenize
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
f = open("text3.txt", 'r')
g = open("ans.txt",'w')
data = f.read()
i = 1 
for p in data.split('\n\n'):   
	for s in tokenizer.tokenize(p.strip()):
		j = 0
		tokens = word_tokenize(s) 
		if(tokens[0]=='Furthermore') or (tokens[0]=='Additionally') or (tokens[0]=='Moreover') or (tokens[0]=='Plus') or (tokens[0]=='Correspondingly'): #add more words later
			g.write("0")
			g.write(" ")
		else:
			g.write("1")
			g.write(" ")
					
		for t in tokens: 
				j = j + 1 
		j = j - 1
		n=str(j)
		g.write(n)
		g.write("\n")
				
