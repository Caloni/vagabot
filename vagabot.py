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

def message(update, context):
    msg = update.message.text
    if msg:
        msg = msg.lower()
        filters = [ 'alguém sabe', 'alguém pode', 'alguém me', 'alguem sabe', 'alguem pode', 'alguem me' ]
        for f in filters:
            if msg.find(f) != -1 and len(msg) != len(f):
                context.bot.send_animation(chat_id=update.effective_chat.id, animation="https://media.giphy.com/media/uDHN0n2COSUhdtwYvM/giphy.mp4", reply_to_message_id=update.message.message_id)
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

