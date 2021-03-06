#coding: utf-8

from scrapy import Spider
from scrapy import log
from scrapy import Request
from credit11315.items import *
import pickle
import  os
import re

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Credit11315(Spider):
    """
    从http://www.11315.com/ranklist/行业名 上抓取
    各公司详细信息的url
    """
    name = 'detail'
    start_urls = ['http://www.11315.com/rankAllList']
    writeInFile = 'all_detail_url'
    download_delay = 30
    def parse(self, response):
        """
        doc
        """
        os.chdir("/home/dyh/data/credit11315")
        with open("all_url_pickle_dump","r") as f:
            cls_dict = pickle.load(f)       #读入各种分类的url
        urls = []
        for li in cls_dict:
            for url in cls_dict[li]:
                urls.append('http://www.11315.com'+url+"?page=100000")
        for url in urls:
            yield Request(url,callback=self.page_parse,dont_filter=True)

    def page_parse(self, response):
        """
        获取不同行业的页面数，并发出请求
        """
        sel = response.selector
        page = sel.xpath(u"//div[@class='paginator']/span[@class='on']/text()").extract()
        try:
            pageNum = int(page[0])
            base_url = response.url[:-6]   #切除掉100000
            for p in range(1, pageNum+1):
                url = base_url + str(p)
                yield Request(url, callback=self.detail_parse,dont_filter=True)
        except Exception,e:
            log.msg("error page_parse error_info=%s" %e, level=log.ERROR)

    def detail_parse(self,response):
        """
        获得不行业公司的url
        """
        sel = response.selector
        urls = sel.xpath(u"//table[@class='listable']/tr/td[2]/a/@href").extract()
        pattern = re.compile(r"http://[\d]{8}\.11315\.com")
        url_concated = ""
        for u in urls:
            if re.match(pattern, u) != None:       #正则判断
                url_concated = url_concated + u + "\n"    #将多个url写入到文件中
            else:
                log.msg("error in detail_parse url=%s" %response.url, level=log.ERROR)
        item = Credit11315Item()
        item['content'] = url_concated
        yield item
