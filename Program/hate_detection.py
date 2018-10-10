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
import numpy as np
import pandas as pd
import matplotlib as plt
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
 

file_data = []
aggressive_tweets = []
targeted_tweets = []

def main():
    targeted_tweets, aggressive_tweets = read_parse("dataset/test/trial_en.tsv")
#    clean_data(tweets)
    
def read_parse(file_name):
    global aggressive_tweets, targeted_tweets
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
            
    """
    Scan through the tweets, and find which ones
    were classified as targeted and hateful.
    - Add flagged aggressive tweets to the aggressive list
    - Add flagged targeted tweets to the targeted list
    """
    
    selected_data = []
    aggressive = []
    targeted = []
    
    for row in file_data:
        row[2] = int(row[2])
        row[3] = int(row[3])
        
        if row[2] == 1:
            targeted.append(row[1])
            
        if row[3] == 1:
            aggressive.append(row[1])
            
    """
    Convert list of lists into strings
    Separate the tweets into specific words before
    cleaning.
    """
    # Gather the tweets: 
    targeted_strings = []
    aggressive_strings = []
    
    for row in targeted:
        targeted_strings.append(row.split("\n"))
        
    for each in targeted_strings:
        targeted_tweets.append("".join(each))
        
    for row in aggressive:
        aggressive_strings.append(row.split("\n"))
        
    for each in aggressive_strings:
        aggressive_tweets.append("".join(each))
        
    """
    Split the categorized tweets into singular words.
    """
    for each in aggressive_tweets:
        aggressive_tweets.append(each.split())
    for each in targeted_tweets:
        targeted_tweets = each.split()

    print(aggressive_tweets)    
    return(targeted_strings, aggressive_strings)

    
#def clean_data(tweets):
#    print(tweets)
#    print("\n\n")
#    set(stopwords.words('english'))
#    for words in tweets:
#        for each in words:
#            filtered
#    print(tweets)
        
main()