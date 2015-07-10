# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
import os
import pickle
os.chdir("/home/dyh/data/credit11315")
class Credit11315Pipeline(object):
    def process_item(self, item, spider):
        try:
            with open("all_url_pickle_dump","a") as f:
                pickle.dump(item["content"], f)
        except Exception,e:
            log.msg("error pipeline error_info=%s"%e, level=log.ERROR)
