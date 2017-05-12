import json

fo = open('french.json', 'r')
fw = open('french.txt', 'a')

for line in fo:
	try:
		tweet = json.loads(line)
		if not tweet['retweeted'] and 'RT @' not in tweet['text']:
			fw.write(tweet['text']+"\n")
	except:
		continue