# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:18:23 2018

@author: Monika Chand
"""

import os
from xml.etree import ElementTree
import pandas as pd


file_name = 'mesa-sleep-0001-profusion.xml'
full_file = os.path.abspath(os.path.join('data\\apnea',file_name))



dom =ElementTree.parse(full_file)
cols = ['Duration', 'Input', 'Name','Start']
df = pd.DataFrame(columns=cols)

scored_event = dom.findall('ScoredEvents/ScoredEvent')
  #cols = ['Duration', 'Input', 'Name','Start']
lst= []
for s in scored_event :
    
#    data =[s.find('Duration').text,s.find('Input').text,s.find('Name').text,s.find('Start').text]
    data =[]
    for c in cols :
       
        data.append(s.find(c).text)
    lst.append(data)
    
df = pd.DataFrame(lst,columns=cols)
    #        print(s.find('Duration').text)
#        print(s.find('Input').text)
#        print(s.find('Name').text)
#        print(s.find('Start').text)



df.to_csv('out_new.csv',encoding='utf-8', index=False)




def xmltocsv(path,cols,tree,out_file):
    dom =ElementTree.parse(path)
    df = pd.DataFrame(columns=cols)
    scored_event = dom.findall(tree)
    lst= []
    for s in scored_event :
        data =[]
        for c in cols :
            data.append(s.find(c).text)
        lst.append(data)
    
    df = pd.DataFrame(lst,columns=cols)
      
    df.to_csv(out_file,encoding='utf-8', index=False)
    print("Output File "+out_file +' created....')


tree ='ScoredEvents/ScoredEvent'
cols = ['Duration', 'Input', 'Name','Start']
xmltocsv(full_file,cols,tree,file_name+'.csv')