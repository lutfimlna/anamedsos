from nltk import word_tokenize, pos_tag, chunk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import RegexpParser, word_tokenize, pos_tag
from nltk import word_tokenize, pos_tag, FreqDist, tag
import json

# tagged_sentence = pos_tag(sentence)
# entities = chunk.ne_chunk(tagged_sentence)
# print (sentence)

fo = open('trump.tweets', 'r')

my_list = list()

#MUST BE HAVE STOPWORD PACKAGE FROM NTLK
infile=open('StopWordEnglish.dic')
stop_words = list()
#Adding stop word data
for line in infile:
    if(line[:-1:] not in stop_words):
    	stop_words.append(line[:-1:])

#DIBAWAH INI MERUPAKAN STOPWORDS REMOVAL
for line in fo:
	try:
		#list temporary untuk menampung kata-kata bebas stopword dalam suatu kalimat
		tempArr = list();

		for tempWord in word_tokenize(str.lower(line)):
			
			#print (tempWord)
			if tempWord not in stop_words and ('https' not in tempWord) and ('//https' not in tempWord) and ('//' not in tempWord) and ('//t.co/' not in tempWord):
				tempArr.append(tempWord)

				#Debug apakah kata ter filter dalam stopwords
				#print (tempWord, 'lolos')

		#print(tempArr)
		my_list.append(tempArr)
	except:
		continue


#print(my_list)

#KODE DIBAWAH INI ADALAH UNTUK MERUBAH KATA KE KATA DASAR
#lemmatization -> mengubah sebuah kata ke kata dasar (lemma) yang ada pada kamus
wordnet_lemmatizer = WordNetLemmatizer()

listSentencePure = list()

for element in my_list:
	tempStr = ""

	for nestedElement in element:
		tempStr += nestedElement + " "

	listSentencePure.append(tempStr[:-1:])


#POSTAGGER
for sentence in listSentencePure:
	tagged = pos_tag(word_tokenize(sentence))

	print ([tag.tuple2str(t) for t in tagged])
		
#TODO AMBIL ADJEKTIVE
#
#
#