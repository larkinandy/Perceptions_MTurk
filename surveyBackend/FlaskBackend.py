#!/usr/bin/env python
# coding: utf-8


import import_ipynb
import WeightedSampling
import random
import uuid 
import os
from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request, url_for, jsonify
from random import randint
from flask_cors import CORS
from collections import deque
import threading

OUTCOME_LABELS = ['greenspace','relax','safe','beauty']
QA_TRANSLATION = ['more cars']


app = Flask(__name__)
CORS(app)





def isCarVoteValid(jsonRecord):
    carIndex = jsonRecord['labels'].index(QA_TRANSLATION[0])
    leftCarImg = jsonRecord['idsLeft'][carIndex]
    carVote = jsonRecord['votes'][carIndex]
    leftImgCat = GameModel.carImgSet.getCarCatByImgId(leftCarImg)

    if(leftImgCat == True):
        if(int(carVote) < 50):
            return(True)
        else:
            return(False)
    else:
        if(int(carVote) >50):
            return(True)
        else:
            return(False)


def convertVoteToOutcome(vote):
    vote = int(vote)
    if(vote==50):
        return(WeightedSampling.Outcomes('tie','tie','tie'))
    if(vote<50):
        print("left side wins")
        if(vote<16):
            return(WeightedSampling.Outcomes('win','win','win'))
        if(vote<33):
            return(WeightedSampling.Outcomes('win','win','tie'))
        return(WeightedSampling.Outcomes('win','tie','tie'))
    else:
        print("right side wins")
        if(vote>84):
            return(WeightedSampling.Outcomes('lose','lose','lose'))
        if(vote>67):
            return(WeightedSampling.Outcomes('lose','lose','tie'))
        return(WeightedSampling.Outcomes('lose','tie','tie'))


def updateTSScores(jsonRecord,GameModel,angle):
    labels = jsonRecord['labels']
    translatedLabels = GameModel.translateLabels(labels,toSurvey=False)[0]
    for index in range(len(labels)):
        currLabel = labels[index]
        currTransLabel = translatedLabels[index]
        if(currLabel != 'more cars'):
            leftId = jsonRecord['idsLeft'][index]
            rightId = jsonRecord['idsRight'][index]
            gameOutcome = convertVoteToOutcome(jsonRecord['votes'][index])
            GameModel.updateGame(currTransLabel,leftId,rightId,gameOutcome,angle)



def processMTRecord(jsonRecord,GameModel):
    imageIds = jsonRecord['idsLeft'] + jsonRecord['idsRight']
    assign_id = str(uuid.uuid1())[:100]
    try:
        temp_id = jsonRecord['turkId']
        if(temp_id != 'None'):
            assign_id = temp_id
    except Exception as e:
        a = e
    angle=jsonRecord['angle']
    didInsertRecord= GameModel.insertMTRecord(assign_id,jsonRecord)
    if not(didInsertRecord):
        print("didn't insert mechanical turk record")
    for image in imageIds:
        GameModel.insertMTToImageRecord(assign_id,image)
    if(isCarVoteValid(jsonRecord)):
        print('car vote is valid.  Will update TS scores')
        updateTSScores(jsonRecord,GameModel,angle)
    else:
        print("car vote isn't valid for assign id" + assign_id + ".  TS scores won't be updated")



@app.route("/")
def hello():
    return "Hello World!"


def addToSample():
    print(len(randomSampleQueue))
    if(len(randomSampleQueue)<10):
        randomIndex = random.randint(0,1)
        randomSampleQueue.append(GameModel.randomlySampleAllLabels(1,randomIndex)[0])
        randomIndexQueue.append(randomIndex)
    print("upated")
    print(len(randomSampleQueue))

@app.route("/sample", methods=['GET'])
def get_sample():
    if(len(randomSampleQueue)>0):    
        randomSample = randomSampleQueue[0]
        randomIndex = randomIndexQueue[0]
        randomSampleQueue.popleft()
        randomIndexQueue.popleft()
    else:
        randomIndex = random.randint(0,1)
        randomSample = GameModel.randomlySampleAllLabels(1,randomIndex)[0]
    randomLabels,grammar = GameModel.translateLabels(randomSample['labels'])
    thread = threading.Thread(target=addToSample)
    thread.start()
    #print(randomSample)
    
    if(randomIndex==1):
        angle='straight'
    else:
        angle='side'
    return {
        "labels" : randomLabels,
        "httpLeft":randomSample['httpLeft'],
        "httpRight":randomSample['httpRight'],
        "idLeft":randomSample['leftIds'],
        "idRight":randomSample['rightIds'],
        "grammar":grammar,
        "angle":angle
    }

@app.route('/sample/submit', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    #print('data from client:' + str(input_json))
    processMTRecord(input_json,GameModel)
    dictToReturn = {'answer':42}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 17995))
    print(PORT)
    GameModel = WeightedSampling.MTGame(OUTCOME_LABELS)
    randomIndex = random.randint(0,1)
    randomSampleQueue = deque(GameModel.randomlySampleAllLabels(1,randomIndex))
    randomIndexQueue = deque([randomIndex])
    for index in range(8):
        randomIndex = random.randint(0,1)
        randomSampleQueue.append(GameModel.randomlySampleAllLabels(1,randomIndex)[0])
        randomIndexQueue.append(randomIndex)
    #from werkzeug.serving import run_simple
    #run_simple('localhost', 5000, app)
    app.run(host='0.0.0.0',port=PORT)

