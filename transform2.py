import json

fo = open('ahok (11-05-2017 pkl 11_35 - 17_36).json', 'r')
fw = open('ahok.tweets', 'a')

for line in fo:
	try:
		tweet = json.loads(line)
		fw.write(tweet['text']+"\n")
	except:
		continue