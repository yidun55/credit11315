# -*- coding: utf-8 -*-

# Scrapy settings for credit11315 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'credit11315'

SPIDER_MODULES = ['credit11315.spiders']
NEWSPIDER_MODULE = 'credit11315.spiders'

DEFAULT_ITEM_CLASS = 'credit11315.items.Credit11315Item'
ITEM_PIPELINES=['credit11315.pipelines.Credit11315Pipeline']

LOG_FILE = "/home/dyh/data/credit11315/log"


DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'credit11315.rotate_useragent.RotateUserAgentMiddleware' :400
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'credit11315 (+http://www.yourdomain.com)'
