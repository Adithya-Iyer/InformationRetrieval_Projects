import glob
import xml.etree.ElementTree as ET
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
from nltk.stem.porter import PorterStemmer

# dir = "/people/cs/s/sanda/cs6322/Cranfield/*" # Comment to run on Local
dir = "Cranfield/*" # Comment to run on csgrads server
collection = glob.glob(dir)

tokenDocs = {'37', '639', '471', '446', '1267'}
stemDocs = {'300', '365', '196', '996', '1152'}
docs = tokenDocs | stemDocs
tokenTokens = []
stemTokens = []
print()

for file in collection:
    
    root = ET.parse(file)
    checkFile = False
    title, text = '', ''
    stem = False
    
    for child in root.findall('*'):
        if(child.tag=='DOCNO'):
            if child.text.strip() in docs:
                checkFile = True
                if child.text.strip() in stemDocs:
                    stem = True
        elif(child.tag=='TITLE') and checkFile:
            title = child.text.strip()
        elif(child.tag=='TEXT') and checkFile:
            txt = child.text.strip()
    
    if checkFile:
        tokens = wordpunct_tokenize(title) + wordpunct_tokenize(txt)
        tokens = [token.lower() for token in tokens]
        english_stopwords = stopwords.words("english")
        tokens = [token for token in tokens if token not in english_stopwords]
        tokens = [token for token in tokens if token not in punctuation]
        if stem:
            stemTokens.extend(tokens)
        else:
            tokenTokens.extend(tokens)

tokenCtr = Counter(tokenTokens)
singleTokens = [ctr[0] for ctr in tokenCtr.most_common() if ctr[1]==1]

print('1. The number of total tokens in the given 5 files =', len(tokenTokens))
print('2. The number of unique tokens in the given 5 files =', len(set(tokenTokens)))
print('3. The number of tokens which occur only once in the given 5 files =', len(singleTokens))
print('4. The 10 most frequent tokens in the given 5 files =', tokenCtr.most_common(10))
print('5. The average number of tokens per document in the given 5 files =', len(tokenTokens)/5)
print()

stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in stemTokens]
stemCtr = Counter(stems)
singleStems = [ctr[0] for ctr in stemCtr.most_common() if ctr[1]==1]

print('1. The number of total stems in the given 5 files =', len(stems))
print('2. The number of unique stems in the given 5 files =', len(set(stems)))
print('3. The number of stems which occur only once in the given 5 files =', len(singleStems))
print('4. The 10 most frequent stems in the given 5 files =', stemCtr.most_common(10))
print('5. The average number of stems per document in the given 5 files =', len(stems)/5)
print()