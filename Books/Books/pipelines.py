# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
   def default(self, o):
       if isinstance(o, Decimal):
           return float(o)
       return super(DecimalEncoder, self).default(o)


class BooksPipeline(object):

    def process_item(self, item, spider):
        r = [item]
        out = json.dumps(r, cls=DecimalEncoder, indent=1, sort_keys=False, ensure_ascii=False).encode('utf8').decode()
        print(out)
