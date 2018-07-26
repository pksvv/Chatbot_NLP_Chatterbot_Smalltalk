#uri = "postgresql://localhost:5432/?user=postgres&password=postgres"
#uri = "postgresql://postgres:postgres@localhost:5432/chatbot"
uri = 'sqlite:///chatbot.db'
database = "chatbot"
trainFile = "talk/chatbot.json"
logpath = "."

app_url = "http://10.32.215.23:8000/smalltalk/"

import logging

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("{0}/{1}.log".format(".", "chatbot"))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

