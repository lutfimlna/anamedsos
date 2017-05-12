file trump.tweets berisi hasil streaming twitter menggunakan tweepy dan telah diambil data textnya.

file maincode.py adalah program yang memproses trump.tweets untuk melakukan sentimen analisis
(Progres: Stop Word Removal, Lemmatization, dan pos tagging)

file streaming.py digunakan untuk streamming tweet pada twitter
file transform2.py digunakan untuk mengambil text dari JSON

file wcn.py digunakan untuk mengambil edges dan nodes pada tweet tersebut, terkait co-occurence

file StopWordEnglish.dic berisi list stopword untuk melakukan stopword removal

file wan-edges.csv dan wan-nodes.csv digunakan untuk melakukan analisis grafik di gephi