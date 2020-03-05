# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import QuoteItem


class SpiderSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, r):
        item = QuoteItem()
        for quote in r.css('.quote'):

            item['text'] = quote.css('.text::text').extract_first()
            item['tags'] = quote.css('.tag::text').extract()

            yield item