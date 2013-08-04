#coding=utf-8
import difflib
import imp
import os
from snowflake.scrapers.scraperbase import scraper

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def get_scrapers_directory():
    return os.path.dirname(os.path.realpath(scraper.__file__))


def get_scraper(scrapername):
    scraper = imp.load_source('snowflake.{0}'.format(scrapername),
                              os.path.join(get_scrapers_directory(), scrapername.lower(), "scraper.py"))

    if scraper.__scrapername__.lower() != scrapername.lower():
        return scraper
    else:
        return scraper


def get_best_from_results(game_searches, game_name):
    best_match = {}
    best_ratio = 0
    for scraper, game_search in game_searches.iteritems():
        try:
            if difflib.SequenceMatcher(None, game_search["title"], game_name).ratio() > best_ratio:
                best_ratio = difflib.SequenceMatcher(None, game_search["title"], game_name).ratio()
                best_match = {"scraper": scraper, "search": game_search}
        except KeyError:
            pass

    return best_match


def get_best_search_result(game_list, game_name):
    best_match = {}
    best_ratio = 0
    for game in game_list:
        if difflib.SequenceMatcher(None, game["title"], game_name).ratio() > best_ratio:
            best_ratio = difflib.SequenceMatcher(None, game["title"], game_name).ratio()
            best_match = game

    return best_match


def get_match_by_threshold(game_dict, game_name, match_threshold):

    return


def format_html_codes(s):
    """
    :author: Angelscry
    Replaces HTML character codes into their proper characters
    :return:
    """
    s = s.replace('<br />', ' ')
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&#039;", "'")
    s = s.replace('<br />', ' ')
    s = s.replace('&quot;', '"')
    s = s.replace('&nbsp;', ' ')
    s = s.replace('&#x26;', '&')
    s = s.replace('&#x27;', "'")
    s = s.replace('&#xB0;', "°")
    s = s.replace('\xe2\x80\x99', "'")
    return s