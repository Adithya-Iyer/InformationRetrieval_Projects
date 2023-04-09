import math
import glob
import xml.etree.ElementTree as ET
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
from nltk.stem.porter import PorterStemmer

# dir = "/people/cs/s/sanda/cs6322/Cranfield/*" # Comment to run on Local
dir = "./Cranfield/*" # Comment to run on csgrads server
collection = glob.glob(dir)
stemmer = PorterStemmer()

numOfDocs = 0
stemTitties = {}
docPussy = {}

for file in collection:
    
    root = ET.parse(file)
    title, text = '', ''
    docID = -1
    numOfDocs += 1
    
    for child in root.findall('*'):
        if(child.tag=='DOCNO'):
            docID = int(child.text.strip())
        elif(child.tag=='TITLE'):
            title = child.text.strip()
        elif(child.tag=='TEXT'):
            txt = child.text.strip()
    
    tokens = wordpunct_tokenize(title) + wordpunct_tokenize(txt)
    tokens = [token.lower() for token in tokens]
    english_stopwords = stopwords.words("english")
    tokens = [token for token in tokens if token not in english_stopwords]
    tokens = [token for token in tokens if token not in punctuation]
    stems = [stemmer.stem(token) for token in tokens]

    docDick = {}
    for stem in stems:
        freq = docDick.get(stem, 0) + 1
        docDick[stem] = freq
        stemDick = stemTitties.get(stem, {})
        stemDick[docID] = freq
        stemTitties[stem] = stemDick
    docPussy[docID] = docDick

docInfo = (446, 886, 930)
termInfo = ('evapor', 'delta', 'help')
comprLst = ('tumbl', 'product', 'precipit')

print('\n\n Document Index Information')

for doc in docInfo:
    docMap = docPussy[doc]
    print('\n For doc', doc)
    doclen = sum(docMap.values())
    print('doclen =', doclen)
    max_tf = max(docMap.values())
    print('max_tf =', max_tf)
    unique_terms = len(set(docMap.keys()))
    print('unique_terms =', unique_terms)

print('\n\n Term Index Information')

for term in termInfo:
    termMap = stemTitties[term]
    postingList = list(sorted(termMap.keys()))
    firstDoc = postingList[0]
    lastDoc = postingList[-1]
    print('\n For term', term)
    print('Document frequency df =', len(termMap))
    print('First doc:', firstDoc, ' and tf =', termMap[firstDoc])
    print('Last doc:', lastDoc, ' and tf =', termMap[lastDoc])

print('\n\n Postings Compression')

def gamma_encode(n):
    if n<=1:
        return '0'
    code = "{0:b}".format(n)
    prefix = ['1']*(len(code)-1)
    code = ''.join(prefix) + '0' + code[1:]
    return code

for word in comprLst:
    termMap = stemTitties[word]
    postingList = list(sorted(termMap.keys()))
    gaps = [postingList[0]]
    for i in range(1, len(postingList)):
        gaps.append(postingList[i]-postingList[i-1])
    gammas = [gamma_encode(gap) for gap in gaps]
    print('\n For word', word, '\nGaps:', gaps, '\nGamma compressed gaps:', gammas)
