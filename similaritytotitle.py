import nltk.data
from nltk import tokenize
import re, math
from collections import Counter
filename = 'C:/Users/Nandash/Desktop/input.txt'
f = open(filename)
data = f.read()
count_sentences = 0

tokens = tokenize.sent_tokenize(data)
for sentence in tokens:
	print sentence+"%d"% count_sentences
	count_sentences = count_sentences + 1
#print "Count %d"% count_sentences
#sentencex=tokens[0]
title= data.rsplit('\n',1)[0]

WORD = re.compile(r'\w+')

#Cosine Similarity
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
	text = text.lower()
	words = WORD.findall(text)
	return Counter(words)

count = 0
for sentence2 in tokens:
	print str(count) + " " +str(get_cosine(text_to_vector(title),text_to_vector(sentence2)))
	count = count + 1