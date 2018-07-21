from nltk.tokenize import word_tokenize
import nltk
def tokenize(string):                                                                   #just converting sentence to words
    print("Tokinizing the sentence................")
    words = word_tokenize(string)
    words.pop()                                                                             # removing ? symbol
    return words

def postag(words):
	print("Tagging sentence and extracting keywords...............")
	tags = nltk.pos_tag(words)
	badwords = ['IN','TO','WP','VBD','DT','VBP','CD','VBZ','WDT','WRB','"',',','(',')',':']	# these pos tagged words are removed
	keywords = []
	for i in tags:
        		if i[1] not in badwords:
           			keywords.append(i[0])
	return keywords

def bigram(keywords):

    '''Converts keywords to bigrams for search.'''
    print("Converting keywords to bigrams...........")
    bigrams = nltk.bigrams(keywords)
    key = []
    for i in bigrams:
    	key.append(i[0]+" "+i[1])                                              #making a search term for wikipedia search

    
    return key
