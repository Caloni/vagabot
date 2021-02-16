#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to vagabonds in groups.

author Wanderley Caloni <wanderley.caloni@gmail.com>
date 2020-11
"""
import re
import sys
import logging
import telegram.ext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
import xml.etree.ElementTree as ET
import argparse
import os

update_id = None
animation_url = "https://media.giphy.com/media/uDHN0n2COSUhdtwYvM/giphy.mp4"

def message(update, context):
    if update.message:
        msg = update.message.text
        if msg:
            msg = msg.lower()
            regex = os.environ["REGEX"] if "REGEX" in os.environ else "(alguem|alguém|someone|anybody|quem)(\s+)(sabe|me|aqui|here|faz|pode|consegue|can|could|sabe|tem|explain|explica|help|ajuda|conhece|manja|que manje|que conheça|que conheca|knows|that knows|que saiba).*\?"
            if re.search(regex, msg, flags=re.MULTILINE | re.IGNORECASE) != None:
                context.bot.send_animation(chat_id=update.effective_chat.id, animation=animation_url, reply_to_message_id=update.message.message_id)

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

