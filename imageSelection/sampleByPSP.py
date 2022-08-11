import pandas as ps
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from copy import deepcopy as dc
import multiprocessing as mp
import globalConstants as gConst
import time

PARENT_FOLDER = gConst.PARENT_FOLDER
CANDIDATE_FILE = PARENT_FOLDER + "CitySideCandidates.csv"
CATEGORIES_OF_INTEREST = ["tree","grass","plant","greenspace","bluespace",
                          "built_env","build2",
                          "animate",
                          "accessibility",
                          "road",
                          "sky"
                          ]
NUM_ITERATIONS = 30000
SAMPLE_SIZE = 227

def calcZScores(inputDataset,categories):
    outputLabels = []
    for cat in categories:
        outputLabel = cat + '_z'
        tempVals = inputDataset[cat]
        meanVals = np.mean(tempVals)
        stdVals = np.std(tempVals)
        zScore = np.divide(np.subtract(tempVals,meanVals),stdVals)
        minScore = min(zScore)
        maxScore = max(zScore)
        totalSpan = maxScore - minScore
        diffPerCat = totalSpan/9
        zScoreMod = np.subtract(zScore,minScore)
        zScoreCat = np.rint(np.divide(zScoreMod,diffPerCat))
        inputDataset[outputLabel] = zScoreCat
        outputLabels.append(outputLabel)
    return([inputDataset,outputLabels])

def calcNumCats(inputData,quantLabels,sampleSize):
    numCats = []
    for val in quantLabels:
        tempVals = inputData[val]
        tempVals = tempVals[np.logical_not(np.isnan(tempVals))]
        numCats.append(10)
    print(numCats)
    return(numCats)

def preProcessInput(inputFile,categories=CATEGORIES_OF_INTEREST,sampleSize=SAMPLE_SIZE):
    rawData = ps.read_csv(inputFile)
    quantData,quantLabels = calcZScores(rawData,categories)
    numCats = calcNumCats(quantData,quantLabels,sampleSize)
    return([quantData,quantLabels,numCats])

def calcDeciles(inputDataset,categories):
    outputLabels = []
    for quanCat in categories:
        categoryLabel = quanCat + '_d'
        inputDataset[categoryLabel] = ps.qcut(inputDataset[quanCat],10,labels=False,duplicates='drop')
        outputLabels.append(categoryLabel)
    return([inputDataset,outputLabels])

def calcScoreOneCat(inputDataset,category,numCats):
    catData = inputDataset[category]
    expectedNumPerCat = len(catData)/(1.0*numCats)
    screenedCatData = catData[~np.isnan(catData)]
    varScore = 0
    for cat in range(0,numCats):
        obsMinExp = sum(catData==cat) - expectedNumPerCat
        singleCatVarScore = (1.0*obsMinExp*obsMinExp)/(1.0*expectedNumPerCat*len(screenedCatData))
        varScore += singleCatVarScore
    return(varScore)

def caclScoresAllCats(inputDataset,categories,numCats):
    categoryScores = []
    currIndex = 0
    for category in categories:
        categoryScores.append(calcScoreOneCat(inputDataset,category,numCats[currIndex]))
        currIndex+=1
    totalScore = sum(categoryScores)/(1.0*len(categories))
    categoryScores.append(totalScore)
    return(categoryScores)

def testOneSubstitutionParallel(bestDataset,categories,subsetDataset,candidateIndex,bestDatasetIndex,numCats):
    candidateDataset = bestDataset.copy(deep=True)
    candidateDataset.iloc[bestDatasetIndex] = subsetDataset.iloc[candidateIndex]
    candidateScores = caclScoresAllCats(candidateDataset,categories,numCats)
    return(candidateScores[len(candidateScores)-1])

def testAllSubstitutionsParallel(bestDataset,bestScores,categories,entireDataset,bestDatasetIndex,numCats):
    curIds = set(list(bestDataset['panid']))
    subsetDataset = entireDataset[~entireDataset['panid'].isin(curIds)]
    pool = mp.Pool(24)
    rangeVals = list(range(0,len(subsetDataset['panid'])))
    results = pool.starmap(testOneSubstitutionParallel,
                           [(bestDataset,categories,subsetDataset,row,bestDatasetIndex,numCats)
                           for row in rangeVals]
                          )
    pool.close()
    pool.join()
    bestVal = min(results)
    if(bestVal < bestScores[len(bestScores)-1]):
        bestDataset.iloc[bestDatasetIndex] = subsetDataset.iloc[results.index(bestVal)]
        newBestScores = caclScoresAllCats(bestDataset,categories,numCats)
        return([bestDataset,newBestScores,True])
    else:
        return([bestDataset,bestScores,False])

def iterateSample(inputDataset,categories,sampleSize,numCats):
    bestSample = inputDataset.iloc[0:sampleSize]
    currIds = list(bestSample['panid'])
    bestScores = caclScoresAllCats(bestSample,categories,numCats)
    currIndex = 1
    sampledIndex = 0
    endIndex = len(bestSample['panid'])
    numIterations = 0
    while(currIndex != sampledIndex and numIterations < SAMPLE_SIZE):
        bestSample,bestScores,didUpdate= testAllSubstitutionsParallel(bestSample,bestScores,categories,inputDataset,currIndex,numCats)
        if(didUpdate): 
            sampledIndex = currIndex
            currIds = list(bestSample['panid'])
            print("bestScores" + str(bestScores))
            if(len(currIds) != SAMPLE_SIZE):
                print("sampled side is too big!" + str(len(currIds)))
        currIndex +=1
        currIndex = currIndex % endIndex
        if(len(currIds) != len(set(currIds))):
            print("failed to prevent duplicates")
            return -1
        if(currIndex % 1) == 0:
            print("currIndex " + str(currIndex) + " sampledIndex " + str(sampledIndex))
            print("numIterations: " + str(numIterations))
        numIterations +=1
    return([bestSample,bestScores])

if __name__ ==  '__main__': 
    quantData,quantLabels,numCats = preProcessInput(CANDIDATE_FILE)
    quantData = shuffle(quantData)
    quantSubset = quantData
    bestSample, bestScores = iterateSample(quantSubset,quantLabels,SAMPLE_SIZE,numCats)
    bestSample.to_csv(PARENT_FOLDER + "CitySideSelected.csv",index=False)
    quantSubset.to_csv(PARENT_FOLDER + "CitySideSelectedzScores.csv",index=False)
