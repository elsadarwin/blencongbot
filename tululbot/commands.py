import re
from urllib.parse import urlencode

from bs4 import BeautifulSoup
import requests

from . import app, bot
from .utils import QuoteEngine


quote_engine = QuoteEngine()


@bot.message_handler(commands=['quote'])
def quote(message):
    app.logger.debug('Detected as quote command')
    return bot.reply_to(message, quote_engine.retrieve_random())


@bot.message_handler(commands=['who'])
def who(message):
    app.logger.debug('Detected as who command')
    about_text = (
        'BlencongBot v1.0.0\n\n'
        'Enhancing your Blencong experience since 2016\n\n'
        'Contribute on https://github.com/elsaadarwin/blencongbot\n\n'
    )
    return bot.reply_to(message, about_text, disable_preview=True)
