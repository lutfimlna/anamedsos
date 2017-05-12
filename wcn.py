from __future__ import division
from sets import Set
import re

def loadTwitterStp(filestp):
    wordSet = Set([])
    file = open(filestp, 'r')
    for line in file:
        line = line.strip().lower()
        wordSet.add(line)
    return wordSet

def tokenizer(sentence):
    SCANNER = re.compile(r'''
        (\s+) |                      # whitespace
        (//)[^\n]* |                 # comments
        0[xX]([0-9A-Fa-f]+) |        # hexadecimal integer literals
        (\d+) |                      # integer literals
        (<<|>>) |                    # multi-char punctuation
        ([][(){}<>=,;:*+-/]"') |     # punctuation
        ([A-Za-z_][A-Za-z0-9_]*) |   # identifiers
        (.)                          # an error!
    ''', re.DOTALL | re.VERBOSE)
    tokens = []
    for match in re.finditer(SCANNER, sentence):
        space, comment, hexint, integer, mpunct, \
        punct, word, badchar = match.groups()
        #if space: tokens.append(space)
        #if comment: tokens.append(comment)
        #if hexint: tokens.append(hexint)
        #if integer: tokens.append(integer)
        #if mpunct: tokens.append(mpunct)
        #if punct: tokens.append(punct)
        if word: tokens.append(word)
    return tokens

stpWordSet = loadTwitterStp('StopWordEnglish.dic')
print (stpWordSet)


def defaultFilterFunc(w):
    return (w not in stpWordSet and ('http' not in w))

def extractPossiblePairs(sentence, filterFunc):
    tupleSet = Set([])
    sentence = tokenizer(sentence.lower())
    words = [w for w in sentence if filterFunc(w)]
    for i in range(0,len(words)):
        for j in range(i+1, len(words)):
            tupleSet.add((words[i], words[j]))
    return tupleSet

def scanTweets(filename, thresholdBottom, thresholdUp):
    tuple_count = {}
    file = open(filename, 'r')
    for line in file:
        tupleSet = extractPossiblePairs(line, defaultFilterFunc)
        for tuple in tupleSet:
            if tuple in tuple_count:
                tuple_count[tuple] += 1
            else:
                tuple_count[tuple] = 1
    #select those tuples whose occurence > threshold
    frequent_tuples = [(tuple,count) for (tuple,count) in tuple_count.items() if ((count >= thresholdBottom) and (count <= thresholdUp))]
    return frequent_tuples

def createEdgeAndNodeList(frequent_tuples, prefixOutFileName):
    #mapping word->id
    word_id = {}
    current_idx = 0
    for (tuple,_) in frequent_tuples:
        word1, word2 = tuple
        if word1 not in word_id:
            current_idx += 1
            word_id[word1] = current_idx
        if word2 not in word_id:
            current_idx += 1
            word_id[word2] = current_idx

    #loop sekali lagi buat NodeList
    fileNode = open(prefixOutFileName+'-nodes.csv', 'w')
    fileNode.write('id;label'+'\n')
    for word in word_id.keys():
        fileNode.write(str(word_id[word])+";"+word+"\n")

    #loop sekali lagi buat EdgeList
    max_weight = max([count for (_,count) in frequent_tuples])
    fileEdge = open(prefixOutFileName+'-edges.csv', 'w')
    fileEdge.write('Source;Target;Type;id;weight'+'\n')
    i = 1;
    for (tuple,count) in frequent_tuples:
        fileEdge.write(str(word_id[tuple[0]])+";"+str(word_id[tuple[1]])+";Undirected;"+str(i)+";"+str(count/max_weight)+'\n')
        i += 1

#Co-occurence minimal '40' maksimal '200'
createEdgeAndNodeList(scanTweets("ahok.tweets", 40, 200), "wan")

