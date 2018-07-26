from django.apps import AppConfig
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
from talk import Parameters
from talk.Parameters import logger
from chatterbot import ChatBot


class TalkConfig(AppConfig):
    name = 'talk'  
    smallTalk_Bot = None      

   # Train chatterbot with JSON corpus 
    def train_smalltalk():
     logger.info ('Training smalltalk in app start up')
     chatbot = ChatBot("SmallTalk_ChatBot",storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri= Parameters.uri)
     chatbot.storage.drop()
    
     chatbot.storage.create()
     logger.info ('Created chatbot database')
     chatbot.set_trainer(ListTrainer)
    
     smallTalkFile = open(Parameters.trainFile, encoding='utf-8')    
     smallTalks = json.load(smallTalkFile)
     logger.info ('Training small talk')
     for key, value in smallTalks.items():
        for item in value:
         logger.debug ('Created chatbot database')
         chatbot.train(item)

    # Initialise chatterbot read only
    def start_SmallTalk_bot():
     TalkConfig.smallTalk_Bot = ChatBot("SmallTalk_ChatBot",storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri= Parameters.uri, read_only=True, logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_random_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.85,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ])
     
    # App start
    def ready(self):
      logger.info ('App ready\n')
      logger.debug ('Parameters.database: '+ Parameters.uri)

      try:
        logger.info ('Training smalltalk in app start up')
        TalkConfig.train_smalltalk()
        TalkConfig.start_SmallTalk_bot()

      except (RuntimeError, TypeError, NameError):
         logger.error ('Exception while training bot')
         pass

    # Get smallTalk_Bot instance
    def get_SmallTalk_bot():
        logger.debug ('get small talk bot')
        
        if TalkConfig.smallTalk_Bot is None:
            logger.info ('smallTalk_Bot not initialised, initialising')
            TalkConfig.start_SmallTalk_bot()

        return TalkConfig.smallTalk_Bot
      
