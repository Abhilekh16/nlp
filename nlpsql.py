
import nltk
from nltk.tag import StanfordPOSTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from datetime import datetime
import os

def tokenize(text):
	tokens=word_tokenize(text)
	stopWords = set(stopwords.words('english'))
	stopWords = stopWords - set(['all','won']) #set(['what','where','when','why','how','and','between'])
	filteredTokens = [word for word in tokens if word not in stopWords]
	return filteredTokens

def lemmatizing(text):
	filteredTokens = tokenize(text)
	lemmatizer = WordNetLemmatizer()
	lematizedToken = [lemmatizer.lemmatize(token) for token in filteredTokens]
	return lematizedToken

def POSTagging(text):
	stanford_dir = "C:/Users/Abhilekh/Desktop/stanford-postagger-full-2018-10-16"
	modelfile = stanford_dir + "/models/english-bidirectional-distsim.tagger"
	jarfile=stanford_dir+"/stanford-postagger.jar"
	tagger=StanfordPOSTagger(model_filename=modelfile, path_to_jar=jarfile)
	java_path = "C:/Java/jdk-9.0.1/bin/java.exe"
	os.environ['JAVAHOME'] = java_path
	lematizedToken = lemmatizing(text)
	tagged = tagger.tag(lematizedToken)
	return tagged


def parse(text):
	tagged = POSTagging(text)
	chunkregex = r"""Chunk: {.?(<VBD>|<VB>)*(<NN>|<NNP>|<JJ>|<CD>)*(<CD>|<NN>|<NNP>|<JJ>)}"""
	chunkParser = nltk.RegexpParser(chunkregex)
	chunked = chunkParser.parse(tagged)
	#chunked.draw()
	return chunked

def returnKeyWord(chunked):
	for chunks in chunked:
		for chunk in chunks:
			if (chunk in ['winner','won','win']):
				return 'winner,Date FROM ipltable'
			elif(chunk is 'venue'):
				return 'venue,Date FROM iplTable'
				return (query)
			elif(chunk is 'city'):
				return 'Distinct city FROM iplTable'
				
			elif(chunk is 'match'):
				return 'team1,team2 FROM iplTable'
				
			elif(chunk is 'date'):
				return 'Date FROM iplTable'
				
			elif(chunk in ['player','man']):
				return 'PLAYER_OF_MATCH FROM iplTable' 
				
	
	return ('wrong input query')

	
def queryGenerator(text):
	chunked=parse(text)

	if(returnKeyWord(chunked) is 'wrong input query' ):
		return 'wrong input query'
		
	query='SELECT'+  ' ' + returnKeyWord(chunked)

	query +=' ' + 'WHERE'
	
	year=place=' '
	
	for chunks in chunked:
		for chunk in chunks:
			if(chunk[1]=='CD'):
				year=chunk[0]
			elif(chunk[1]== 'NN' or chunk[1]=='NNP' or chunk[1]=='JJ' or chunk[1]=='NNS'):
				place=chunk[0]

	
	query +=' '+'city = ' +'\''+ (place[0].upper()+place[1:]) +'\'' +' AND season = '+year
	
	return query

	
print(queryGenerator("winner of the match played in Hyderabad in 2017"))