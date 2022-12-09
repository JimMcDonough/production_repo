# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:29:44 2022

@author: jimmc
"""
from flask import Flask, jsonify, request
from transformers import TFAutoModelForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline

app = Flask(__name__)


@app.route('/')
def Question_Answer():
    
    question = request.args.get('question')
    context = request.args.get('context')
    
    if not isinstance(question, str) or not isinstance(context, str):
        return jsonify(message="question and context must be strings"), 400
   
    elif (question is None) or (context is None):
        return jsonify(message="question and context cannot be None type"), 400
    
    elif len(question) == 0 or len(context) == 0:
        return jsonify(message="question and context cannot be of length 0"), 400
    
    else:
        model = TFAutoModelForQuestionAnswering.from_pretrained(r'full_saved_model')
        tokenizer = AutoTokenizer.from_pretrained(r'full_saved_model')
        
        question_answerer = pipeline(task="question-answering", model=model, tokenizer=tokenizer)
        
        
        return jsonify(question_answerer(question=question,context=context))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)