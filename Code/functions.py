import keras
import os
import spacy
from pathlib import Path
import time
import warnings
import pandas as pd

OUTPUT1='NER Models/Name/content/Model'
OUTPUT2='NER Models/Prefix/content/Model'
OUTPUT3='NER Models/Position Held/Model'
OUTPUT4='NER Models/Intelligence/Model'

    
nlp_Name = spacy.load(OUTPUT1)
nlp_Pref = spacy.load(OUTPUT2)
nlp_Min = spacy.load(OUTPUT3)
nlpIntel = spacy.load(OUTPUT4)
#adding animated titles
# importing the necessary packages 
import time 
import sys 
import os 
  
# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "starting your console application..."
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 100): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
  
    # Your desired code continues from here  
    # s = input("Enter your name: ") 
    s ="David"
    sys.stdout.write("Hello "+str(s)+"\n") 


def pred(tag):
    tag = tag.strip().lower()
    stop_words = ["external website"]
    for sw in stop_words:
        if sw in tag:
            return 0
    if(tag.isnumeric()):
        return 1
    doc = nlpIntel(tag)
    #print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    for ent in doc.ents:
        if ent.text!=0:
            #print(tag)
            return 1
    return 0
