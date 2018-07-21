from nltk.corpus import PlaintextCorpusReader as pr
import nltk
import math
#exit()

	#-----------------------calculate TF-IDF-----------------------------#
def calculateScore(tf,df):			# given TF and DF claculating tf-idf for each document 
	temp = []
	for i in tf.keys():
		#print('\n',i)
		s = 0
		for j in df.keys():
			try:
				score = (1+math.log( tf[i][j] / sum(tf[i].values()) )) / ( math.log(1 / df[j]) )	#try to write it mathematically
				s += score
				#print(j,score,sep='-')
			except:
				pass
		print(i,'--->',s,sep=' ')		#printing each document score
		temp.append((i,s))
	return temp


def get_files():
	root = "./doc"
	para_list = pr(root,'.*')
	fileslist = para_list.fileids()
	#print(fileslist)
	return root,para_list,fileslist

def unigrams(keys):

	root,para_list,fileslist = get_files()		# try yourself
	
	df = {}
	tf = {}
	for i in keys:
		df[i.lower()] = 0
		
	for i in fileslist:
		word = para_list.words(i)

		tf[i] = {}
	#----------calculate df of each word in the question----------------------#
		for j in set(word):
			j = j.lower()
			try:
				df[j] += 1
			except:
				pass

		for j in df.keys():
			tf[i][j] = 0
		for k in word:
			k = k.lower()
			try:
				tf[i][k] += 1
			except:
				pass

	score = calculateScore(tf,df)
	
	return score

# unigrams(['What','is','the','oldest','structure','at','Notre','Dame'])

def bigrams(keys):			# try yourself
	
	root,para_list,fileslist = get_files()
	
	df = {}
	tf = {}
	keys = list(nltk.bigrams(keys))
	for i in keys:
		i = i[0]+' '+i[1]
		df[i.lower()] = 0
		
	for i in fileslist:
		word = para_list.words(i)
		word = list(nltk.bigrams(word))
		bigram =[]
		for j in word:
			bigram.append(j[0]+' '+j[1])
		tf[i] = {}
	#----------calculate df of each word in the question----------------------#
		for j in set(bigram):
			j = j.lower()
			try:
				df[j] += 1
			except:
				pass

		for j in df.keys():
			tf[i][j] = 0
		for k in bigram:
			k = k.lower()
			try:
				tf[i][k] += 1
			except:
				pass
	score = calculateScore(tf,df)
	return score

# bigrams(['What','is','the','oldest','structure','at','Notre','Dame'])