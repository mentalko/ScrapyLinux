# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SpiderSpider(CrawlSpider):
    name = 'crawler'
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
        title = r.xpath('//div/h1/text()').extract_first()
        image = r.xpath('//div[@class="item active"]/img/@src').extract_first()
        price = r.xpath('//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract_first()
        stock = r.xpath('//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()')\
            .extract()[1].strip()
        stars = r.xpath('//div/p[contains(@class, "star-rating")]/@class').extract_first()\
            .replace('star-rating','')
        description = r.xpath('//div[@id="product_description"]/following-sibling::p/text()').extract_first()

        TABLE_SELECTOR = '//table[@class="table table-striped"]'
        ups = r.xpath(TABLE_SELECTOR + '/tr[1]/td/text()').extract_first()
        price_excl_tax = r.xpath(TABLE_SELECTOR + '/tr[3]/td/text()').extract_first()
        price_incl_tax = r.xpath(TABLE_SELECTOR + '/tr[4]/td/text()').extract_first()
        tax = r.xpath(TABLE_SELECTOR + '/tr[5]/td/text()').extract_first()

        yield {
            'Title': title,
            'Image': r.urljoin(image),
            'Price': price,
            'Stock': stock,
            'Stars': stars,
            'Description': description,
            'UPS': ups,
            'Price excl tax': price_excl_tax,
            'Price incl tax': price_incl_tax,
            'Tax': tax,
        }

