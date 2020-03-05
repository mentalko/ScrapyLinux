# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import BooksItem


class SpiderSpider(CrawlSpider):
    name = 'itemcrawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = [
        Rule(LinkExtractor(allow='catalogue/',
                           restrict_xpaths='.//ol[@class="row"]'),
             callback='parse_book', follow=False),
        Rule(LinkExtractor(restrict_xpaths='.//a[text()="next"]'),
             follow=True)
        ]

    def parse_book(self,r):
        item = BooksItem()
        item['title'] = r.xpath('//div/h1/text()').extract_first()
        item['image'] = r.xpath('//div[@class="item active"]/img/@src').extract_first()
        item['price'] = r.xpath('//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract_first()
        yield item