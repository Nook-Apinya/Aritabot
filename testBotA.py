from flask import Flask,request,abort
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)

from linebot.models import (
  MessageEvent,TextMessage,TextSendMessage,
)

app=Flask(__name__)

line_bot_api = LineBotApi('qBpiQjKeUZOKYG1jc1jMOcMEFJs3p7BLv7g8ZH8JC5qGVQSv4XDwHAgRtWGr463O/r5NE4cJXpw/NPVUCenl2z6Cwis6m8HVvmG8ftku7Z9SvpORORlaR0BEF5L//YJH4Eaf48h3achDqmeiEppn7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cbe045731caced5c132e9b3e51aa7178')

line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))

#try:
    #line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))
#except LineBotApiError as e:
    #print("Got Error")