'''
        Main script to run Document Retriever.
                                                            '''
import os
#import scripts.extract as extract
#mport scripts.getArticle as getArticle
import questionProcessor as QP
import articleExtractor as AE
import TF_IDF
import json
import glob
def main(question):
    
    '''Main function.'''
    print("----------------------------------------------Document Retriever--------------------------------------------------")
    p = glob.glob("doc/*")
    for i in p:
    	os.remove(i)

    # question = input("Enter the question to be searched: ")	#take question input form user ? should be there

    tokens = QP.tokenize(question)				#converting sentence into words thats it

    keywords = QP.postag(tokens)				#eliminating some keywords based on parts of speech tagging

    if(len(keywords) == 0):     					# if pos tagging eliminates all the word
        keywords = tokens

    query_keys = QP.bigram(keywords)				# making search keys into two keys to search wikipedia

    if(len(query_keys) == 0):       					# if there is only one key element bigram cannot happen
        query_keys = keywords

    print("search keys are : ",query_keys)					

#---------------------------Question Processing  Done-------------------------#

    n = AE.getArticles(query_keys)				# gets the article soupifies and writes to a file under doc folder
    print("Fetched ",n, "articles",sep = ' ')				# just printing how many articles v fetched
    
    #-------------------------------TF-IDF-------------------------------------------#
    
    print('\n--------unigram rank---------')
    score = TF_IDF.unigrams(tokens)					# it is as it seems

    max_score = score[0][1]
    max_score_id_uni = score[0][0]
    for i in range(1,len(score) - 1):
    	if(score[i][1] > max_score):
    		max_score = score[i][1]
    		max_score_id_uni = score[i][0]
    print("analysinig :",max_score_id_uni,sep = " ")

    max_score_id_uni = "0.txt"
    print('\n---------bigram rank---------')
    score = TF_IDF.bigrams(tokens)

    max_score = score[0][1]
    max_score_id_bi = score[0][0]
    for i in range(1,len(score) - 1):
    	if(score[i][1] > max_score):
    		max_score = score[i][1]
    		max_score_id_bi = score[i][0]
    print("analysing : ",max_score_id_bi,sep = " ")		# lets try unigram bigram and also trigram hashing

    max_score_id_bi = "0.txt"
    # one for unigram
    d = {"data" : [{"title" : max_score_id_uni,"paragraphs":[]}],"version":"1.1"} 
    f = open("doc/"+max_score_id_uni,"r",encoding= "utf8").read()
    temp = f.split("\n")
    count = 0 

    for i in temp:
    	if(len(i) > 0):
	    	temp = {"context":i,"qas" :[{"answers" : [{"answer_start" : 123 ,"text" : "actual answer ends"}],
	    								  "question": question,
	    								  "id" : str(count)
	    								  }]}
	    	d["data"][0]["paragraphs"].append(temp)
	    	count += 1	    	
    
    # once for bigram file
    f = open("doc/"+max_score_id_bi,"r",encoding= "utf8").read()
    temp = f.split("\n")
    count = 0 
    for i in temp:
    	if(len(i) > 0):
	    	temp = {"context":i,"qas" :[{"answers" : [{"answer_start" : 123 ,"text" : "actual answer ends"}],
	    								  "question": question,
	    								  "id" : str(count)
	    								  }]}
	    	d["data"][0]["paragraphs"].append(temp)
	    	count += 1

    p = open("data/squad/train-v1.1.json","w")
    p.write(json.dumps(d))
    p.close()
    os.system("qa_answer.py")
    try:
        with open('dev-prediction1.json', 'r') as ansFile:
            answerFile = json.load(ansFile)
        print(answerFile["1"],answerFile["2"],answerFile["3"])
        if(tokens[0] == "who"):
            return answerFile["1"]
        elif(tokens[0] == "when"):
            return answerFile["3"]
        elif(tokens[0] == "where"):
            return answerFile["4"]
        else:
            with open('dev-prediction.json', 'r') as ansFile:
                answerFile = json.load(ansFile)
            return answerFile["0"] #+"\n"+answerFile["1"]+"\n"+answerFile["2"]+"\n"+answerFile["3"]+"\n"+answerFile["4"]+"\n"+answerFile["5"]+"\n"
    except NameError:
        with open("dev-prediction.json", 'r') as ansFile:
            answerFile = json.load(ansFile)
        return answerFile["0"]

    

if __name__ == '__main__' :
    main()
    
