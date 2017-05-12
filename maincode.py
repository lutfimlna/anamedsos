from nltk import word_tokenize, pos_tag, chunk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
import json

# tagged_sentence = pos_tag(sentence)
# entities = chunk.ne_chunk(tagged_sentence)
# print (sentence)

fo = open('ahok2 (tgl 12 pkl 11_30 - 15_29).json', 'r')
fw = open('french.txt', 'a')

my_list = list()


for line in fo:
	try:
		my_list.append(word_tokenize(json.loads(line)['text']))
	except:
		continue



#KODE DIBAWAH INI ADALAH UNTUK MERUBAH KATA KE KATA DASAR
#lemmatization -> mengubah sebuah kata ke kata dasar (lemma) yang ada pada kamus
wordnet_lemmatizer = WordNetLemmatizer()

for element in my_list:
	for nestedElement in element:
		print(nestedElement,"->",wordnet_lemmatizer.lemmatize(nestedElement))