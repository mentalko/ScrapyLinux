# -*- coding: utf-8 -*-
import base64

import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

from w3lib.http import basic_auth_header
import js2xml
from googletrans import Translator


class SpiderSpider(scrapy.Spider):
    name = 'tabirai'
    allowed_domains = ['www.tabirai.net']
    start_urls = ['https://www.tabirai.net/hotel/']

    def parse(self, response):
        for item in response.xpath('.//p[@class="areaImg"]'):
            subpage_url = item.xpath('.//a/@href').extract_first() + 'search/result.aspx'
            if subpage_url: 
                yield response.follow(subpage_url, callback=self.parse_subpage)

    def parse_subpage(self, response):
        perfecture = response.xpath('.//a[@class="gaHeaderStayPC"]/text()').extract_first()
        number = response.xpath('.//p[@class="number"]/span/text()').extract_first()

        tran = Translator()

        yield {'perfecture:': tran.translate(perfecture).text,
               'count:': number}
