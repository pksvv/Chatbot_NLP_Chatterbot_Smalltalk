# -*- coding: utf-8 -*-
from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
from talk import Parameters
from talk.apps import TalkConfig

from talk.Parameters import logger
import time
import re

#Get small talk response from trained corpus
def get_chatbot_response(textmessage):
    
    chatbot = TalkConfig.get_SmallTalk_bot()
  
    response = chatbot.get_response(textmessage)
   
    logger.debug (response.confidence)
    if (response.confidence < .85):
      logger.error ('\nLow confidence -->' + textmessage)

    return(str(response))


def get_SmallTalk_response(inputString):
   
    resp = 'I am sorry, but I do not understand.'
    logger.info ('Smalltalk input : '+ inputString)
    
    try:
       inputString = re.sub(r'[^\w]', ' ', inputString)
       inputString = re.sub(' +',' ', inputString)
       logger.debug ('Smalltalk input : '+ inputString)
       start = time. time()
       resp = get_chatbot_response(inputString)
       logger.info ('Smalltalk response : ' + resp)
       
       end = time. time()
       logger.info  ('\nResponse time --->'+ str((end - start)))
       logger.info (resp)
    except (RuntimeError, TypeError, NameError):
       
       logger.error ('Exception while getting response')

    return resp



