# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:48:09 2022

@author: jimmc
"""
import json
import random
import os


#verify the json matches the Squad format
def verfifySqaudDatasetKeys(dataset):
    
    if not isinstance(dataset, dict):
        return False
    
    if not 'data' in dataset.keys():
        return False
    
    if not set(dataset['data'][0].keys()) == {'paragraphs', 'title'}:
        return False
    
    if not set(dataset['data'][0]['paragraphs'][0].keys()) == {'qas', 'context'}:
        return False
    
    if not set(dataset['data'][0]['paragraphs'][0]['qas'][0].keys()) == {'question', 'id', 'answers', 'is_impossible'}:
        return False
    
    if not set(dataset['data'][0]['paragraphs'][0]['qas'][0]['answers'][0].keys()) == {'answer_start', 'text'}: 
        return False
    
    return True
    
#JSON format to use in Transformaers library
def reform_json(sample):
    
    splitqandas = []
    for topic in sample:
        title = topic['title']
        for qasandcontext in topic['paragraphs']:
            context = qasandcontext['context']
            for qas in qasandcontext['qas']:
                if qas['is_impossible']:
                    qas['answers'].append({'text':'', 'answer_start':0})
                    qadict = {}
                    qadict['answers'] = qas['answers']
                    qadict['context'] = context
                    qadict['id'] = qas['id']
                    qadict['question'] = qas['question']
                    qadict['title'] = title
                    splitqandas.append(qadict)
                else:
                    qadict = {}
                    qadict['answers'] = qas['answers']
                    qadict['context'] = context
                    qadict['id'] = qas['id']
                    qadict['question'] = qas['question']
                    qadict['title'] = title
                    splitqandas.append(qadict)
    
    return splitqandas 


def createTrainValTestSplit(dataPath, randseed = 31, saveDirectory = '', train_per=.8, val_per=.10, test_per=.10):
     
    if not  os.path.isfile(dataPath):
        raise Exception("Path entered is not a file or does not exist.")
    
    if not train_per + val_per + test_per == 1:
         raise Exception("Percents must sum to one.")
    
    try:    
        
        with open(dataPath, 'r') as f:
            json_data = json.load(f)
            
    except:
        raise Exception("Json Format Error!")
    
    
    if not verfifySqaudDatasetKeys(json_data):
        raise Exception('Incorrect SQUAD JSON format!')
        
    random.seed(randseed)
    
    indexes = list(range(len(json_data['data'])))
    random.shuffle(indexes)

    train_cut = int(train_per*len(json_data['data']))
    val_cut = train_cut + int(val_per*len(json_data['data']))
    test_cut = val_cut + int(test_per*len(json_data['data']))
    
    train = indexes[:train_cut]
    val = indexes[train_cut:val_cut]
    test = indexes[val_cut:test_cut]
    
    train_data = [json_data['data'][i] for i in train]
    val_data = [json_data['data'][i] for i in val]
    test_data = [json_data['data'][i] for i in test]
    
    train_data_reform =  reform_json(train_data)
    val_data_reform =  reform_json(val_data)
    test_data_reform =  reform_json(test_data)

    if saveDirectory:
        if not os.path.exists(saveDirectory):
            raise Exception("Save Path does not exist")
            
        with open(saveDirectory + r'/train.json', 'w') as outfile:
            json.dump(train_data_reform, outfile)

        with open(saveDirectory + r'/val.json', 'w') as outfile:
            json.dump(val_data_reform, outfile)
            
        with open(saveDirectory + r'/test.json', 'w') as outfile:
            json.dump(test_data_reform, outfile)
            
    return train_data_reform, val_data_reform, test_data_reform

