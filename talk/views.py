from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from talk import smalltalkbot

from talk.Parameters import logger


@csrf_exempt
def getSmallTalkResponse(request, inputString):
    
    logger.debug ('Request reached in smalltalk views')
    logger.info ('User input -->'+ inputString )
    response = smalltalkbot.get_SmallTalk_response(inputString)
    logger.debug ('response -->'+ response )

    return HttpResponse( response)
