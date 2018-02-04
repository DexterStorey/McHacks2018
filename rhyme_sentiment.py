import requests 
import json
import sys
import random
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn

def useDatamuse(word1, word2):
	site = 'https://api.datamuse.com/words?' + word2
	json_data = requests.get(site + word1 + '&max=10').text
	data = json.loads(json_data)
	if(data.__len__()>1) :
		num = random.randint(0, 9)
		output = data[num]['word']
		return output
	elif (data.__len__() == 1):
		num = 0
		output = data[num]['word']
		return output
	else :
		return None 

def findSynonym(word):
	return useDatamuse(word, 'ml=')

def findAntonym(word):
	return useDatamuse(word, 'rel_ant=')

def findRhyme(word):
	return useDatamuse(word, 'rel_rhy=')

def findApproxRhyme(word):
	return useDatamuse(word, 'rel_nry=')

def findNextWord(word):
	return useDatamuse(word, 'rel_bga=')

def getAdj(word):
	return useDatamuse(word, 'rel_jjb=')

def makeMeanPhrase(word):
	adj = getAdj(word)
	new_word = findSynonym(word)
	phrase = "You think I'm a " + word + "?\n" + "Well, you're a " + adj + " " + new_word + " from nowhere" 
	return phrase

print(makeMeanPhrase('box'))