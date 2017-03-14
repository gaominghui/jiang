#-*- coding:utf-8 -*-
'''
@author: gaominghui
'''
from objc._objc import NULL
from __builtin__ import list
import xlwt
import xlrd
import numpy as np
import os
import sys
import random
from itertools import count

kaijiangriqi=[]
kaijianghaoma=[]

def jiang():
    global kaijiangriqi
    global kaijianghaoma
    count =0
    data=xlrd.open_workbook("/Users/gaominghui/git/neural-networks-and-deep-learning/data/history.xlsx",'r')
    table = data.sheets()[0]
    nrows=table.nrows
    count=0;
    for i in range(nrows):
            count=count+1
            kaijiangriqi.append( str(int(table.row_values(i)[0])))
            l=str(table.row_values(i)[1]).split("|")[0].split(",")
            e = np.zeros((34, 1))
            for i in range(6):
                e[int(l[i])]=1.0
            kaijianghaoma.append(e)
    kaijianghaoma.reverse()
    kaijianghaoma_temp=[]
    for i in range(1,len(kaijianghaoma)):
        kaijianghaoma_temp.append(kaijianghaoma[i])
  
    kaijianghaoma_temp.append(np.zeros((34, 1)))
    training_data=zip(kaijianghaoma[0:-10],kaijianghaoma_temp[0:-10])
    test_data=zip(kaijianghaoma[-10:],kaijianghaoma_temp[-10:])
    return (training_data, test_data, test_data)



def jiang2(src,k):
    global kaijiangriqi
    global kaijianghaoma
    count =0
    data=xlrd.open_workbook(src,'r')
    table = data.sheets()[0]
    nrows=table.nrows
    count=0;
    for i in range(nrows):
            count=count+1
            kaijiangriqi.append( str(int(table.row_values(i)[0])))
            l=str(table.row_values(i)[1]).split("|")[0].split(",")
            e = np.zeros((34, 1))
            for i in range(6):
                e[int(l[i])]=1.0
            kaijianghaoma.append(e)
    kaijianghaoma.reverse()
    
    kaijianghaoma_temp=[]
    for i in range(k,len(kaijianghaoma)):
        arr_temp=[]
        for j in range(i-k,i):
            for ele in kaijianghaoma[j]:
                arr_temp.append(ele[0])
        
        kaijianghaoma_temp.append(np.array(arr_temp).reshape(k*34,1))

    
    training_data=zip(kaijianghaoma_temp[0:-10],kaijianghaoma[k:-10])
    test_data=zip(kaijianghaoma_temp[-10:],kaijianghaoma[-10:])
    arr_temp=[]
    for temp in kaijianghaoma[-k:]:
        for i in temp:
            arr_temp.append(i[0])

    test_data.append( (np.array(arr_temp).reshape(k*34,1),np.zeros((34,1))) )
    return (training_data, test_data, test_data)


    
    

'''
def ran():

    list=[]
    ret=[]
    global kaijiangriqi
    global kaijianghaoma

    for i in range(1,34):
      list.append(i)
    slice=sorted(random.sample(list,6))
    ran_str=",".join(str(t).zfill(2) for t in slice )+"|"+str(random.randint(1,16)).zfill(2)
   
    count=0;
    while(ran_str!=kaijianghaoma[0].strip()):
         slice=sorted(random.sample(list,6))
         ran_str=",".join(str(t).zfill(2) for t in slice )+"|"+str(random.randint(1,16)).zfill(2)
         count+=1
         print ran_str+"\t"+kaijianghaoma[0].strip()
    print "begin -------"
    while(i in range(1,len(kaijianghaoma)-1)):
        count=0
        while(ran_str!=kaijianghaoma[i].strip()):
            slice=sorted(random.sample(list,6))
            ran_str=",".join(str(t).zfill(2) for t in slice )+"|"+str(random.randint(1,16)).zfill(2)
            count+=1
        print ran_str+"\t"+kaijianghaoma[i].strip()
        print count
'''     
    
    
if __name__ == '__main__':
   jiang2("/Users/gaominghui/git/neural-networks-and-deep-learning/data/history.xlsx",2)
   print 'done'
            
