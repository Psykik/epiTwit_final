def preprocess(X):
    documents = []
    from nltk.stem import WordNetLemmatizer
    import re

    from spacy.lang.en.stop_words import STOP_WORDS
    stopwords = list(STOP_WORDS)

    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):
        document = "{}{}".format(" ", str(X[sen]))
    
        #remove usernames 
        document = re.sub(r'(\s)@\w+', r'\1', document)
    
        #remove links
        document = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', document)
    
        #removing all special characters 
        document = re.sub(r'\W', ' ', document)
    
        #removing all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
        #removing single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    
        #substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags = re.I)
    
        #removing stop words
        remove = '|'.join(stopwords)
        document = re.sub(r'\b('+remove+r')\b', ' ', document, flags = re.IGNORECASE)
    
        #converting to lowercase
        document = document.lower()
        
        #lemmatization
        document = document.split()
    
        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
    
        documents.append(document)
    return(documents)