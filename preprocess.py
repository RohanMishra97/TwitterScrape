import csv
import re
import pandas as pd

#Regex Credits- https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/
regex_str = [
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s):
    #Strip whitespace
    s = s.strip('\n')
    s = s.strip('\t')
    #Tokenize tweet
    tokens = tokenize(s)
    #Drop all mentions
    s = " ".join([token for token in tokens if token[0] != '@'])
    return s

filename = "tweets.csv"
data = pd.read_csv(filename)
data[data.columns[0]] = data[data.columns[0]].apply(preprocess)
data.to_csv("processed.csv")
print ("Data Preprocessed")
