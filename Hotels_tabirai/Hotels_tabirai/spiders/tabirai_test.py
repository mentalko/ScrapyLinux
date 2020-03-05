# -*- coding: utf-8 -*-
import base64

import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

from w3lib.http import basic_auth_header

class SpiderSpider(scrapy.Spider):
    name = 'tabirai_test'
    allowed_domains = ['www.tabirai.net']
    start_urls = ['https://www.tabirai.net/']

    # def start_requests(self):
    #     meta={"proxy": "http://nl.free.zoogvpn.com:1194"}
    #     headers = {
    #         'Proxy-Authorization': basic_auth_header(
    #             'is.omskas@gmail.com', 'palypass')
    #     }
    #     yield Request(self.start_urls[0], headers=headers, meta=meta)

    def parse(self, response):
        MAP_XPATH = './/dl[@class="pl-springboardBox"]'
        print('+++++++++++++++')

        for item in response.xpath(MAP_XPATH):
            # subpage_url = category.css(SUBPAGE_LINK_CSS).extract_first()
            text = item.xpath('dd[@class="pl-springboardBox__content"]/text()')
            if text:
                yield {'text' : text.extract_first().strip()}

        # title = r.xpath('//div/h1/text()').extract_first()
        # image = r.xpath('//div[@class="item active"]/img/@src').extract_first()
        # price = r.xpath('//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract_first()
        # stock = r.xpath('//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()')\
        #     .extract()[1].strip()
        # stars = r.xpath('//div/p[contains(@class, "star-rating")]/@class').extract_first()\
        #     .replace('star-rating','')
        # description = r.xpath('//div[@id="product_description"]/following-sibling::p/text()').extract_first()
        #
        # TABLE_SELECTOR = '//table[@class="table table-striped"]'
        # ups = r.xpath(TABLE_SELECTOR + '/tr[1]/td/text()').extract_first()
        # price_excl_tax = r.xpath(TABLE_SELECTOR + '/tr[3]/td/text()').extract_first()
        # price_incl_tax = r.xpath(TABLE_SELECTOR + '/tr[4]/td/text()').extract_first()
        # tax = r.xpath(TABLE_SELECTOR + '/tr[5]/td/text()').extract_first()

        # yield {
        #     'Title': title,
        #     'Image': r.urljoin(image),
        #     'Price': price,
        #     'Stock': stock,
        #     'Stars': stars,
        #     'Description': description,
        #     'UPS': ups,
        #     'Price excl tax': price_excl_tax,
        #     'Price incl tax': price_incl_tax,
        #     'Tax': tax,
        # }

