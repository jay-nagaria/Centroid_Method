

import data_handler_almost as DH
import csv
import math
import operator
import numpy



def euclideanDistance(t1,t2):
    distance = 0
    #print(len(t1))
    #print(len(t2))
    for x in range(1,len(t2)-1):
        #print(repr(float(t1[x]))+" - "+repr(float(t2[x])))
        distance += math.pow(float(t1[x])-float(t2[x]),2)
    return math.sqrt(distance)

def myknnclassify(trainingSet, test,Centroid):

 
    bst =100000000000
    val =""
    for key , value in Centroid.items():
        dist = euclideanDistance(Centroid[key],test)
        if dist< bst:
                bst = dist
                val = key
    
    return (val)
            
#print(testSet[32])
#print(val)
#print(testSet[1][-1])

def faccuracy(testSet, prediction):
    All = true_prediction = 0
    for x in range(len(testSet)):
        if testSet[x][0] == prediction[x]:
            true_prediction += 1
        All += 1
    return (true_prediction/All)*100



#new = list(feature_value.keys())


def centroid_1(dataset,trainingSet,testSet):
    feature_value = {}
    for x in range(len(trainingSet)):
        	dummy = trainingSet[x][0]
        	if dummy in feature_value:
        		feature_value[dummy].append(trainingSet[x])
        	else:
        		feature_value[dummy] = []
    Centroid = {}
    for key , value in feature_value.items():
        Next = []
        #print (feature_value[key])
        for x in range (1,len(feature_value[key][0])):#...1  2 ?.....
            tm = 0
            for Xx in range (len(feature_value[key])):
                tm = tm + feature_value[key][Xx][x]
             
            Next.append(tm/len(feature_value[key])) 
        Centroid[key] = Next      
    #print(Centroid)
    
    predictions=[]
    
    for x in range(len(testSet)):
        result = myknnclassify(trainingSet, testSet[x],Centroid)
        predictions.append(result)
        #print(repr(result)+" - "+repr(testSet[x][-1]))
    accuracy = faccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    return(accuracy)
	


trainingSet=[]
testSet=[]
dataset1=[]
                

'''..........................K fold Validation............................'''
'''
list_1=DH.letter_2_digit_convert('ABCDE')
dataset=DH.pickDataClass('G:\Programs\ATNTFaceImages400.txt')

fold=5
accuracy=0.0
for x in range(fold):
    DH.splitData2TestTrain(dataset,10,[2*x,2*(x+1)],trainingSet,testSet)
    
    accuracy=accuracy+centroid_1(dataset,trainingSet,testSet)
    trainingSet=[]
    testSet=[]
print('Final-Accuracy: ' + repr(accuracy/5) + '%')
'''
'''.........................../kfold..................................'''
'''................................normal..............................'''

list_1=DH.letter_2_digit_convert('ABCDE')
dataset=DH.pickDataClass('G:\Programs\HandWrittenLetters.txt',list_1)
#dataset=DH.pickDataClass('G:\Programs\ATNTFaceImages400.txt')
print(len(dataset))
DH.splitData2TestTrain(dataset,39,[31,39],trainingSet,testSet)
               
print ('Training set: ' + repr(len(trainingSet)))
print ('Testing set: ' + repr(len(testSet)))

accuracy=centroid_1(dataset,trainingSet,testSet)

'''............................./normal..................................'''
