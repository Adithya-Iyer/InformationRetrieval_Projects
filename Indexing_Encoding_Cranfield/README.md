# Indexing and Encoding the Cranfield Collection - Information Retrieval

#### The task is to index and encode the stems/lemmas from the tokens in the Cranfield collection of documents. 

### Steps involved:

1.  In the Cranfield collection the document and field boundaries are indicated with SGML tags ("document markup"). SGML tags are not considered words, so they should not be tokenized and included in any of the information your program gathers. The SGML tags in this data follow the conventional style: <[/]?tag> | >[/]?tag (attr[=value])+>
2.  The attributes and the values from the SGML conventional style are optional and appear rarely or not at all in this document collection. We will therefore only consider the TITLE and TEXT tags in this assignment, as both the title and the text of each document contains valuable information for indexing and retrieval.
3.  We use the BeautifulSoup library to parse the SGML tags. We require the use of NLTK's word punctuation tokenizer, which utilizes REGEX to tokenize words and punctuation. This tokenizer is available in the nltk.tokenize module.
4.  Additionally, we convert all text to lowercase before tokenizing. Finally, remove all stopwords and punctuation from the tokens. A list of stopwords is available in the nltk.corpus.stopwords module. A list of punctuation is available in the string module.
5.  Tokenize all the documents present in the Cranfield collection.
6.  Perform stemming and lematization on the tokens. Store the lemmas and tokens information separately.
    * We require the use of NLTK's PorterStemmer stemmer. This stemmer is available in the nltk.stem.porter module.
    * We also require NLTK's WordNet lemmatizer. The lemmatizer is available in the nltk.stem module.
7.  Index the collection. For every entry in the dictionary, store:
    * Document frequency (df): The number of documents that the stem/lemma occurs in.
    * The list of documents containing the stem/lemma.
8.  For each document in the posting lists you are also required to store:
    * The document ID, where the file name is cranfieldXXXX, the integer form of XXXX is the document ID and should be converted to an integer (e.g., cranfield0001 -> 1, cranfield0002 -> 2, etc);
    * The lemma frequency (tf): The number of times that the lemma occurs in that document;
    * Tthe frequency of the most frequent lemma in that document (max_tf);
    * The total number of lemma occurrences in the document (doclen).
    * The number of unique lemmas in the document (unique_terms).
9.  Perform gap compression on the posting lists in the inverted index. 
    * Postings compression is a technique used to reduce the size of the index by reducing the size of postings lists. 
    * One of the most common compression techniques is to store only the difference between consecutive document IDs in the posting list (the gaps).
10. Then use gamma encoding on the compression lists.
    * Gamma encoding is a compression technique that is commonly used to compress integers. 
    * Gamma encoding is a variable length encoding scheme.

**** We are interested in retrieving Document Index Information, Term Index Information, Postings Lists, and Gamma-encoded Compressions.
