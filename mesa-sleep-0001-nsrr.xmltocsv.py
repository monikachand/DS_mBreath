

import os
from xml.etree import ElementTree
import pandas as pd


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
   
    cols = ['Duration','Stages','Start','Type']
    df = pd.DataFrame(lst[1:],columns=cols)
      
    df.to_csv(out_file,encoding='utf-8', index=False)
    print("Output File "+out_file +' created....')





file_name = 'mesa-sleep-0001-nsrr.xml'
full_file = os.path.abspath(os.path.join('data\\stage',file_name))

tree ='ScoredEvents/ScoredEvent'
cols = ['Duration','EventConcept','Start','EventType']
xmltocsv(full_file,cols,tree,file_name+'.csv')