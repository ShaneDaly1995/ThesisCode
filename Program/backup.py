#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:27:02 2018

@author: shanedaly
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:49:35 2018
    
ID [TAB] Tweet [TAB] TR(1/0) [TAB] AG(1/0) 

- a numeric ID that uniquely identifies the tweet within the dataset (id column)
- the text of the tweet (text column)
- a binary value {1|0} indicating if hate speech is occurring against one of 
  the given targets, women or immigrants (HS column)
- if HS occurs (i.e. the value for the feature at point 2 is 1), a binary value 
  indicating if the target is a generic group of people (0) or a specific 
  individual (1) (TR column)
- if HS occurs (i.e. the value for the feature at point 2 is 1), a binary value
  indicating if the tweeter is aggressive (1) or not (0) (AG column)

@author: shanedaly
"""

import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
 
vocab = set()
file_data = []
tweets = []
def main():
    file_data, vocab = read_parse("dataset/test/trial_en.tsv")
#    clean_data(tweets)
    
def read_parse(file_name):
    global tweets, file_data
    """
    Read in the file, remove the first line and append
    to the file_data list. 
    """
    with open(file_name) as tsvfile:
        # Chew up the first line. 
        tsvfile.readline()
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        
        for row in tsvfile:
            file_data.append(row)
       
        for tweet in file_data:
            tweets.append(row)
#    file_data = file_data.split()
      
    """
    Scan through the tweets, and find which ones
    were classified as targeted and hateful.
    - Add those to the selected data list. 
    """
    selected_data = []
    aggressive = []
    targeted = []
    
    for row in file_data:
        row[2] = int(row[2])
        row[3] = int(row[3])
        if row[2] == 1:
            aggressive.append(row[1])
        if row[3] == 1:
            targeted.append(row[1])
            
    vocab.update(aggressive)
    vocab.update()
            
#    """
#    Separate the tweets into specific words before
#    cleaning.
#    """
#    # Gather the tweets: 
#    for row in aggressive, targeted:
#        tweets.append(row.split())
        
    return(file_data, tweets)

    
#def clean_data(tweets):
#    print(tweets)
#    print("\n\n")
#    set(stopwords.words('english'))
#    for words in tweets:
#        for each in words:
#            filtered
#    print(tweets)
        
main()