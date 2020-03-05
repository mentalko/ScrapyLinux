# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


class BooksItem(Item):
    title = Field(input_pocessor=TakeFirst())
    image = Field()
    price = Field()
    stock = Field()
    descriptio = Field()
    ups = Field()
    price_excl_tax = Field()
    price_incl_tax = Field()
    tax = Field()