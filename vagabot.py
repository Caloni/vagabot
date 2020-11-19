#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to vagabonds in groups.

author Wanderley Caloni <wanderley.caloni@gmail.com>
date 2020-11
"""
import sys
import logging
import telegram.ext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
import xml.etree.ElementTree as ET
import argparse

update_id = None
animation_url = "https://media.giphy.com/media/uDHN0n2COSUhdtwYvM/giphy.mp4"

def message(update, context):
    msg = update.message.text
    if msg:
        msg = msg.lower()
        someone = [ 'alguém', 'alguem', 'someone' ]
        can = [ 'sabe', 'pode', 'me', 'consegue', 'can', 'aqui', 'here', 'faz' ]
        for s in someone:
            if msg.find(s) != -1:
                for c in can:
                    if msg.find(c) != -1:
                        if len(msg) > (len(s) + len(c) + len(' ')):
                            context.bot.send_animation(chat_id=update.effective_chat.id, animation=animation_url, reply_to_message_id=update.message.message_id)
                            break

def main():

    argparser = argparse.ArgumentParser('Vaga BOT')
    argparser.add_argument('--auth', help="Telegram authorization token.")
    params = argparser.parse_args()

    updater = Updater(token=params.auth, use_context=True)
    updater = Updater(token=params.auth, use_context=True)
    dispatcher = updater.dispatcher

    message_handler = MessageHandler(callback=message, filters=telegram.ext.filters.Filters.all)
    dispatcher.add_handler(message_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

