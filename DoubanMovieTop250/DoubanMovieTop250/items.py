# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    #排名
    ranking = scrapy.Field()

    movie_name = scrapy.Field()

    score = scrapy.Field()

    score_num = scrapy.Field()
    
    pass
