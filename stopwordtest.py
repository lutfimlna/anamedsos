from nltk.corpus import stopwords
# ...

word_list = ['i', 'love', 'you']
filtered_words = [word for word in word_list if word not in stopwords.words('StopWordEnglish.d')]

