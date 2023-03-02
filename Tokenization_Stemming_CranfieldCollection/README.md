# Tokenization and Stemming the Cranfield Collection - Information Retrieval

#### The task is to tokenize and gather information about tokens in the Cranfield collection of documents. We also stem the tokens in documents from the Cranfield collection and gather information.

### Steps involved:

1. In the Cranfield collection the document and field boundaries are indicated with SGML tags ("document markup"). SGML tags are not considered words, so they should not be tokenized and included in any of the information your program gathers. The SGML tags in this data follow the conventional style: <[/]?tag> | >[/]?tag (attr[=value])+>
2. The attributes and the values from the SGML conventional style are optional and appear rarely or not at all in this document collection. We will therefore only consider the TITLE and TEXT tags in this assignment, as both the title and the text of each document contains valuable information for indexing and retrieval.
3. We use the BeautifulSoup library to parse the SGML tags. We require the use of NLTK's word punctuation tokenizer, which utilizes REGEX to tokenize words and punctuation. This tokenizer is available in the nltk.tokenize module.
4. Additionally, we convert all text to lowercase before tokenizing. Finally, remove all stopwords and punctuation from the tokens. A list of stopwords is available in the nltk.corpus.stopwords module. A list of punctuation is available in the string module.
5. Use the program to tokenize the title and the text of the documents: (cranfield0037, cranfield0639, cranfield0471, cranfield0446, cranfield1267).
6. We require the use of NLTK's PorterStemmer stemmer. This stemmer is available in the nltk.stem.porter module.
7. Use the program to stem the tokens from the title and the text of the documents: (cranfield1152, cranfield0300, cranfield0365, cranfield0196, cranfield0996).
