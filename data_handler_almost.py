# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:39:36 2018

@author: Ashok
"""

import csv
import math
import operator
import random as rnd


trainingSet=[]
testSet=[]

'''........................... Dataset .........................'''
def pickDataClass(filename,class_ids=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40',]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        #print(type(lines))
        dataset1 = list(lines)
        #print(type(dataset1))
        dataset=[list(i) for i in zip(*dataset1)]
        for x in range(len(dataset)):
            for y in range(1,len(dataset[0])):
                dataset[x][y] = float(dataset[x][y])
        new_dataset=[]
        for x in range(len(dataset)):
            if dataset[x][0] in class_ids:
                new_dataset.append(dataset[x])
    #print(new_dataset)    
    return(new_dataset)
    
  
'''---------------SUB 2 ----------'''    


def splitData2TestTrain(filename,no_per_class,test_instances,trainingSet,testSet):
    
    for x in range(len(filename)):
        
        if x%no_per_class >= test_instances[0] and x%no_per_class <= test_instances[1]:
            testSet.append(filename[x])
        else:
            trainingSet.append(filename[x])
            

'''-----------------SUB 3-------------'''

def TestTrainFile(trainingset,testset):
    with open('trainingset.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        trainingset=[list(i) for i in zip(*trainingset)]
        writer.writerows(trainingset)
    with open('testset.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        testset=[list(i) for i in zip(*testset)]
        writer.writerows(testset)

'''..................SUB 4..............'''

def letter_2_digit_convert(word):
    
    
    #print(len(word))
    list_1=[]
    temp=word.lower()
    for x in range(len(temp)):
        list_1.append(str(ord(temp[x])-96))
    #print(list_1)
    return(list_1)
'''..............Accuracy..................'''    
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
    
    
#print("sdf")
#list_1=letter_2_digit_convert('ABCDE')
#dataset=pickDataClass('G:\Programs\HandWrittenLetters.txt',list_1)
#print(len(dataset))